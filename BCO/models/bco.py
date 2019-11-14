from utils import *
import gym
# Debug
import time

class BCO():
  def __init__(self, state_shape, action_shape, lr=0.002, maxits=1000, M=1000):
    # set initial value
    self.state_dim = state_shape            # state dimension
    self.action_dim = action_shape          # action dimension
    self.lr = lr                            # model update learning rate
    self.maxits = maxits                    # maximum iteration
    self.batch_size = args.batch_size       # batch size
    self.alpha = 0.01                       # alpha = | post_demo | / | pre_demo |
    self.M = M                              # sample to update inverse dynamic model

    # initial session
    config = tf.ConfigProto()  
    config.gpu_options.allow_growth=True
    self.sess = tf.Session(config=config)

    # set the input placeholder
    with tf.variable_scope("placeholder") as scope:
      self.state = tf.placeholder(tf.float32, [None, self.state_dim], name="state")
      self.nstate = tf.placeholder(tf.float32, [None, self.state_dim], name="next_state")
      self.action = tf.placeholder(tf.float32, [None, self.action_dim], name="action")
    
    # build policy model and inverse dynamic model
    self.build_policy_model()
    self.build_idm_model()

    # tensorboard output
    writer = tf.summary.FileWriter("logdir/", graph=self.sess.graph)

    self.test_time = 100

  def load_demonstration(self):
    """Load demonstration from the file"""
    if args.input_filename is None or not os.path.isfile(args.input_filename):
      raise Exception("input filename does not exist")

    with open(args.input_filename, 'rb') as f:
      expert_data = pickle.load(f)
      inputs = expert_data['observations']
      targets = expert_data['observations_next']

    num_samples = len(inputs)
    print("Loaded %d demonstrations" % num_samples)    

    return num_samples, inputs, targets

  def sample_demo(self):
    """sample demonstration"""
    sample_idx = range(self.demo_examples)
    sample_idx = np.random.choice(sample_idx, self.num_sample)
    S = [ self.inputs[i] for i in sample_idx ]
    nS = [ self.targets[i] for i in sample_idx ]
    return S, nS

  def build_policy_model(self):
    """buliding the policy model as two fully connected layers with leaky relu"""
    raise NotImplementedError

  def build_idm_model(self):
    """building the inverse dynamic model as two fully connnected layers with leaky relu"""
    raise NotImplementedError

  def eval_policy(self, state):
    """get the action by current state"""
    return self.sess.run(self.policy_pred_action, feed_dict={
      self.state: state
    })

  def eval_idm(self, state, nstate):
    """get the action by inverse dynamic model from current state and next state"""    
    return self.sess.run(self.idm_pred_action, feed_dict={
      self.state: state,
      self.nstate: nstate
    })

  def pre_demonstration(self):
    """uniform sample action to generate (s_t, s_t+1) and action pairs"""
    raise NotImplementedError

  def post_demonstration(self, M):
    """using policy to generate (s_t, s_t+1) and action pairs"""
    raise NotImplementedError

  def eval_rwd_policy(self):
    """getting the reward by current policy model"""
    raise NotImplementedError
    
  def update_policy(self, state, action):
    """update policy model"""
    num = len(state)
    idxs = get_shuffle_idx(num, self.batch_size)
    for idx in idxs:
      batch_s = [  state[i] for i in idx ]
      batch_a = [ action[i] for i in idx ]
      self.sess.run(self.policy_train_step, feed_dict={
        self.state : batch_s,
        self.action: batch_a
      })      
 
  def update_idm(self, state, nstate, action):
    """update inverse dynamic model"""
    num = len(state)
    idxs = get_shuffle_idx(num, self.batch_size)
    for idx in idxs:
      batch_s  = [  state[i] for i in idx ]
      batch_ns = [ nstate[i] for i in idx ]
      batch_a  = [ action[i] for i in idx ]      
      self.sess.run(self.idm_train_step, feed_dict={
        self.state : batch_s,
        self.nstate: batch_ns,
        self.action: batch_a
      })

  def get_policy_loss(self, state, action):
    """get policy model loss"""
    return self.sess.run(self.policy_loss, feed_dict={
      self.state: state,
      self.action: action
    })

  def get_idm_loss(self, state, nstate, action):
    """get inverse dynamic model loss"""
    idm_loss = self.sess.run(self.idm_loss, feed_dict={
      self.state: state,
      self.nstate: nstate,
      self.action: action
    })
    return idm_loss

  def train(self):
    """training the policy model and inverse dynamic model by behavioral cloning"""    
    
    if args.savedPreModel:
      # Use saved pre-demo trained model
      saver_pre = tf.train.Saver()
      saver_pre.restore(self.sess, args.premodel_dir)
      print("\n[Training]")
      print('Loaded pre demo model')
    else:
      # Start session
      self.sess.run(tf.global_variables_initializer())

      print("\n[Training]")
      # pre demonstration to update inverse dynamic model
      S, nS, A = self.pre_demonstration()      
      self.update_idm(S, nS, A)
      # Save pre-demo trained model
      print('saving pre demo model')
      saver_pre = tf.train.Saver(max_to_keep=1)
      saver_pre.save(self.sess, args.premodel_dir)        
    
    # Init model saver
    saver = tf.train.Saver(max_to_keep=1)    

    for it in range(self.maxits):
      def should(freq):
        return freq > 0 and ((it+1) % freq==0 or it == self.maxits-1 )

      # update policy pi
      S, nS = self.sample_demo()
      A = self.eval_idm(S, nS)
      currTime = time.time()
      self.update_policy(S, A)
      
      # Print time taken for debug
      if (args.printTime and should(args.print_freq)):
        print("Policy Learning time: ", time.time() - currTime)
      
      # Check loss on another data set.................
      S, nS = self.sample_demo()
      A = self.eval_idm(S, nS)
      # ...............................................
      policy_loss = self.get_policy_loss(S, A)

      # update inverse dynamic model
      S, nS, A = self.post_demonstration(self.M)
      currTime = time.time()
      self.update_idm(S, nS, A)
      
      # Print time taken for debug
      if (args.printTime and should(args.print_freq)):
        print("Model Learning time: ", time.time() - currTime)
      #idm_loss = self.get_idm_loss(S, nS, A)

      if should(args.print_freq):
        policy_reward = self.eval_rwd_policy()

        # Check loss on another data set.................
        S, nS, A = self.post_demonstration(int(round(self.M * 0.15))) # 15% test data
        idm_loss = self.get_idm_loss(S, nS, A)
        # ...............................................
        print('iteration: %5d, total reward: %5.1f, policy loss: %8.6f, idm loss: %8.6f' % ((it+1), policy_reward, policy_loss, idm_loss))

      # saving model
      if should(args.save_freq):
        print('saving model')
        saver.save(self.sess, args.model_dir)

      # Debug
      # After 20 iterations, redo pre demo learning
      #if should(20):
      #  S, nS, A = self.pre_demonstration()
      #  self.update_idm(S, nS, A)


  def test(self):
    saver = tf.train.Saver()
    saver.restore(self.sess, args.model_dir)
    print('\n[Testing]\nFinal reward: %5.1f' % self.eval_rwd_policy())

  def run(self):
    if not os.path.exists(args.model_dir):
      os.makedirs(args.model_dir)

    if args.mode == 'test':
      if args.model_dir is None:
        raise Exception("checkpoint required for test mode")    

      self.test()

    if args.mode == 'train':
      if args.premodel_dir is None:
        raise Exception("pre-model directory required for saving initial trained model")
      if not os.path.exists(args.premodel_dir):
        os.makedirs(args.premodel_dir)

      # read demonstration data
      self.demo_examples, self.inputs, self.targets = self.load_demonstration()      
      #self.num_sample = self.M  # Issue: This should not directly be set to M, too low in some cases and too high in some cases!!!
      self.num_sample = min(self.demo_examples,self.M)      

      self.train()

