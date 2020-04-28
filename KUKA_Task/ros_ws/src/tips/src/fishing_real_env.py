"""
ROS Interface for Fishing Task using KUKA lbr iiwa 7

Uses iiwa_stack:
https://github.com/IFL-CAMP/iiwa_stack
"""

import rospy
import actionlib
from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import String, Float32
import std_srvs.srv
# tf2_msgs/TFMessage
import numpy as np
import time

BALL_ORIGIN = np.array([0.682839, 0.000187, 0.256688])
GLASS_ORIGIN = np.array([0.746410,0,0.06])
J2_Z_ORIGIN = 0.34
END_EFF_Z_MIN = 0.15
THETA1 = (45 * (np.pi /180)) # Joint 2 initial position
THETA2 = (45 * (np.pi /180)) # Joint 4 initial position
L1 = 0.4   # Length of arm 1
L2 = 0.4   # Length of arm 2
L3 = 0.126 # Length of arm 3
EPISODE_DURATION = 25 # seconds
# ACTION_START_TIME = 0.01 # seconds
ACTION_DURATION = 0.1 # seconds

class Fishing_Env():
    
    def __init__(self):
        rospy.init_node('tips_fishing', anonymous=True, disable_signals=True) # disable rospy handling of Ctrl+C
        
        self.start_time = time.time()
        self.terminal = True # Need to call reset first to start the environment

        ### Joint States
        self.joint_position = np.zeros(7) # Seven joints of the KUKA
        self.joint_velocity = np.zeros(7) # Seven joints of the KUKA
        self.joint_effort = np.zeros(7) # Seven joints of the KUKA
        # Subscriber for joint states:
        rospy.Subscriber('iiwa/joint_states', JointState, self.joint_states_callback, queue_size=1)

        # Subscriber for tfs, tf_static to compute end-effector position in x-z plane
        # rospy.Subscriber('end_eff_tf', String, callback, queue_size=1)

        ### Ball state
        self.ball_position = np.zeros(3) # x,y,z position
        self.ball_velocity = np.zeros(3) # x,y,z velocity
        # Subscriber for ball pose, twist
        rospy.Subscriber('odom/ball', Odometry, self.odom_ball_callback, queue_size=1)

        ### Publisher for controller commands
        self.action_pub = rospy.Publisher('/iiwa/PositionJointInterface_trajectory_controller/command', JointTrajectory, queue_size=1)
        # Command Goal
        self.goal = JointTrajectory()
        # self.goal.header.stamp = rospy.get_rostime() + rospy.Duration.from_sec(ACTION_START_TIME)
        self.goal.joint_names.append("iiwa_joint_1")
        self.goal.joint_names.append("iiwa_joint_2")
        self.goal.joint_names.append("iiwa_joint_3")
        self.goal.joint_names.append("iiwa_joint_4")
        self.goal.joint_names.append("iiwa_joint_5")
        self.goal.joint_names.append("iiwa_joint_6")
        self.goal.joint_names.append("iiwa_joint_7")

        self.goal.points.append(JointTrajectoryPoint())
                                            # joint 2      # joint 4
        self.goal.points[0].positions =  [0,    0      ,0,     0     ,0,0,0]
        self.goal.points[0].velocities = [0,    0      ,0,     0     ,0,0,0]
        self.goal.points[0].time_from_start = rospy.Duration.from_sec(ACTION_DURATION)
        
        # Wait for gazebo simulation
        print("[Waiting for gazebo...]")
        rospy.wait_for_service('gazebo/reset_simulation')
        
        ### Service caller for the reset of Gazebo simulation
        self.reset_sim = rospy.ServiceProxy('gazebo/reset_simulation', std_srvs.srv.Empty())

        ### Service caller to pause/unpasue physics
        self.pause = rospy.ServiceProxy('gazebo/pause_physics', std_srvs.srv.Empty())
        self.unpause = rospy.ServiceProxy('gazebo/unpause_physics', std_srvs.srv.Empty())


    def curr_state(self):
        return np.array([
            self.joint_position[1], # Joint 2
            self.joint_position[3], # Joint 4
            self.joint_velocity[1], # Joint 2
            self.joint_velocity[3], # Joint 4
            self.ball_position[0] - GLASS_ORIGIN[0],  # Ball x position
            self.ball_position[2] - GLASS_ORIGIN[2]  # Ball z position
            # self.ball_velocity[0],  # Ball x velocity
            # self.ball_velocity[2]   # Ball z velocity
        ])


    def reset(self):
        ### Service call to un-pause physics
        self.unpause()
        # Optional: WAIT for controller to be ready
        time.sleep(0.1)

        ### Take action to reset to zero position (with randomization)
        self.goal.points[0].positions =  [0, np.random.uniform(-0.1,0) ,0, np.random.uniform(0, 0.1) ,0,0,0]
        # Optional : Move joint 6 to make ball move more aggresively
        self.goal.points[0].positions[5] = np.random.uniform(-1.5707, 1.5707)
        # Send Action command
        # self.goal.header.stamp = rospy.get_rostime() + rospy.Duration.from_sec(ACTION_START_TIME)
        self.action_pub.publish(self.goal)
        # Wait for action completion
        time.sleep(2*ACTION_DURATION)
        # Optional : Move joint 6 to make ball move more aggresively
        self.goal.points[0].positions[5] = 0
        self.action_pub.publish(self.goal)
        # Wait for action completion
        time.sleep(ACTION_DURATION + 0.1)

        ### Optional: Service call to reset Gazebo sim: Messes with time though
        # self.reset_sim()
        # Optional: WAIT (till a new joint state and ball odom is received)
        # time.sleep(0.01)
        
        # Set time for this episode
        self.start_time = time.time()

        # Reset terminal state
        self.terminal = False

        return self.curr_state()


    def step(self, a):
        vec = self.ball_position - GLASS_ORIGIN # distance vector between ball and cup
        reward_dist = - np.linalg.norm(vec)
        reward_ctrl = - np.square(a).sum()
        reward = reward_dist + reward_ctrl
        
        if (self.terminal):
            print("[Environment terminated. reset() needs to be called before environment can be run]")
        else:
            ### Take action a
            # Sanity check
            if((a >= -0.5).all() and (a <= 0.5).all()):
                # Set goal: Relative position change
                j2_goal = self.goal.points[0].positions[1] +  a[0]
                j4_goal = self.goal.points[0].positions[3] +  a[1]

                if not (j2_goal > (THETA1 - (np.pi/2)) and j2_goal < THETA1):
                    j2_goal = self.goal.points[0].positions[1] # Unchanged
                    print("[Action outside joint limits]")
                if not (j4_goal > (THETA2 - (np.pi/2)) and j4_goal < THETA2):
                    j4_goal = self.goal.points[0].positions[3] # Unchanged
                    print("[Action outside joint limits]")
                
                # Check for end-effector collision:
                _, z_goal = self.get_end_eff_pos(np.array([[j2_goal, j4_goal]]))
                if(z_goal >= END_EFF_Z_MIN):
                    # Accepted (command within limits)
                    self.goal.points[0].positions[1] =  j2_goal
                    self.goal.points[0].positions[3] =  j4_goal
                else:
                    print("[End Effector: minimum height reached]")

                # Send Action command
                # self.goal.header.stamp = rospy.get_rostime() + rospy.Duration.from_sec(ACTION_START_TIME)
                self.action_pub.publish(self.goal)
                # Wait for action completion
                time.sleep(ACTION_DURATION)
                # Optional: WAIT (till a new joint state and ball odom is received)
            else:
                print("[Action provided is too large]")

            # Check if terminal based on total time elapsed since reset
            if ((time.time() - self.start_time) > EPISODE_DURATION):
                self.terminal = True
                # Pause physics
                self.pause()

        return self.curr_state(), reward, self.terminal, dict(reward_dist=reward_dist, reward_ctrl=reward_ctrl)



    ### Callbacks for subscribers

    def joint_states_callback(self, joint_state_msg):
        self.joint_position = np.array(joint_state_msg.position)
        self.joint_velocity = np.array(joint_state_msg.velocity)
        self.joint_effort = np.array(joint_state_msg.effort)

        # Debug print:
        # print("Positions: " + "\n" + str(self.joint_position) + "\n" + "Vels: " + "\n" + str(self.joint_velocity) + "\n" + "Efforts: " + "\n" + str(self.joint_effort))

    def odom_ball_callback(self, odom_msg):
        self.ball_position = np.array([odom_msg.pose.pose.position.x, odom_msg.pose.pose.position.y, odom_msg.pose.pose.position.z])
        self.ball_velocity = np.array([odom_msg.twist.twist.linear.x,odom_msg.twist.twist.linear.y,odom_msg.twist.twist.linear.z])

        # Debug print:
        # print("Positions: " + "\n" + str(self.ball_position) + "\n" + "Vels: " + "\n" + str(self.ball_velocity))

    ## Transform for end-effector position
    def get_end_eff_pos(self, state):
        """get x-z cartesian position of the end effector"""

        theta1 = THETA1 - state[:,0]
        theta2 = THETA2 - state[:,1]

        xpos = L1*np.cos(theta1) + L2*np.cos(theta1-theta2) + L3*np.sin(theta1-theta2)
        zpos = J2_Z_ORIGIN + L1*np.sin(theta1) + L2*np.sin(theta1-theta2) - L3*np.cos(theta1-theta2)

        return xpos, zpos