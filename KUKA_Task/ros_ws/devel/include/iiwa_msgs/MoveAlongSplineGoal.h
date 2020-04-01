// Generated by gencpp from file iiwa_msgs/MoveAlongSplineGoal.msg
// DO NOT EDIT!


#ifndef IIWA_MSGS_MESSAGE_MOVEALONGSPLINEGOAL_H
#define IIWA_MSGS_MESSAGE_MOVEALONGSPLINEGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <iiwa_msgs/Spline.h>

namespace iiwa_msgs
{
template <class ContainerAllocator>
struct MoveAlongSplineGoal_
{
  typedef MoveAlongSplineGoal_<ContainerAllocator> Type;

  MoveAlongSplineGoal_()
    : spline()  {
    }
  MoveAlongSplineGoal_(const ContainerAllocator& _alloc)
    : spline(_alloc)  {
  (void)_alloc;
    }



   typedef  ::iiwa_msgs::Spline_<ContainerAllocator>  _spline_type;
  _spline_type spline;





  typedef boost::shared_ptr< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> const> ConstPtr;

}; // struct MoveAlongSplineGoal_

typedef ::iiwa_msgs::MoveAlongSplineGoal_<std::allocator<void> > MoveAlongSplineGoal;

typedef boost::shared_ptr< ::iiwa_msgs::MoveAlongSplineGoal > MoveAlongSplineGoalPtr;
typedef boost::shared_ptr< ::iiwa_msgs::MoveAlongSplineGoal const> MoveAlongSplineGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace iiwa_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'iiwa_msgs': ['/home/snehal/Desktop/Thesis/IfO/KUKA_Task/ros_ws/src/iiwa_stack/iiwa_msgs/msg', '/home/snehal/Desktop/Thesis/IfO/KUKA_Task/ros_ws/devel/share/iiwa_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e8dcbe6f289dcd0d4eb11721725f5ca8";
  }

  static const char* value(const ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe8dcbe6f289dcd0dULL;
  static const uint64_t static_value2 = 0x4eb11721725f5ca8ULL;
};

template<class ContainerAllocator>
struct DataType< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "iiwa_msgs/MoveAlongSplineGoal";
  }

  static const char* value(const ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Goal\n"
"Spline spline\n"
"\n"
"\n"
"================================================================================\n"
"MSG: iiwa_msgs/Spline\n"
"# The describes a motion along a spline\n"
"\n"
"SplineSegment[] segments\n"
"================================================================================\n"
"MSG: iiwa_msgs/SplineSegment\n"
"# This message describes a segment of a spline path\n"
"\n"
"int32 SPL = 0\n"
"int32 LIN =  1\n"
"int32 CIRC = 2\n"
"\n"
"# The type of the spline segment\n"
"int32 type\n"
"\n"
"# The endpoint of the current segment\n"
"CartesianPose point\n"
"\n"
"# Auxiliary point. Only used for circular segments\n"
"CartesianPose point_aux\n"
"================================================================================\n"
"MSG: iiwa_msgs/CartesianPose\n"
"# Target Pose including redundancy information.\n"
"geometry_msgs/PoseStamped poseStamped\n"
"\n"
"# If you have issues with the robot not executing the motion copy this value from the Cartesian Position Tab of the\n"
"# robot SmartPad. Set both parameters to -1 to disable them.\n"
"RedundancyInformation redundancy\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/PoseStamped\n"
"# A Pose with reference coordinate frame and timestamp\n"
"Header header\n"
"Pose pose\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
"\n"
"================================================================================\n"
"MSG: iiwa_msgs/RedundancyInformation\n"
"# E1 parameter\n"
"# Specifies Angle of the elbow joint.\n"
"float64 e1\n"
"\n"
"# Status parameter\n"
"#   Bit 0: 1 - The robot is working above its head\n"
"#          0 - The robot is working in the ground area\n"
"#   Bit 1: 1 - Angle A4 < 0°\n"
"#          0 - Angle A4 >= 0°\n"
"#   Bit 2: 1 - Angle A6 <= 0\n"
"#          0 - Angle A6 > 0\n"
"int32 status\n"
"\n"
"# Turn parameter\n"
"# According to Sunrise handbook this is not used for the iiwa.\n"
"int32 turn\n"
;
  }

  static const char* value(const ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.spline);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MoveAlongSplineGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::iiwa_msgs::MoveAlongSplineGoal_<ContainerAllocator>& v)
  {
    s << indent << "spline: ";
    s << std::endl;
    Printer< ::iiwa_msgs::Spline_<ContainerAllocator> >::stream(s, indent + "  ", v.spline);
  }
};

} // namespace message_operations
} // namespace ros

#endif // IIWA_MSGS_MESSAGE_MOVEALONGSPLINEGOAL_H
