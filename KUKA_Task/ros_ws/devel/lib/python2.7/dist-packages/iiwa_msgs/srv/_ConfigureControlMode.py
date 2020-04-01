# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from iiwa_msgs/ConfigureControlModeRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import iiwa_msgs.msg

class ConfigureControlModeRequest(genpy.Message):
  _md5sum = "5e02ca4e5bba97a102b6f5d4c0a7fc99"
  _type = "iiwa_msgs/ConfigureControlModeRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """


int32 control_mode
iiwa_msgs/JointImpedanceControlMode joint_impedance
iiwa_msgs/CartesianImpedanceControlMode cartesian_impedance
iiwa_msgs/DesiredForceControlMode desired_force
iiwa_msgs/SinePatternControlMode sine_pattern
iiwa_msgs/CartesianControlModeLimits limits

================================================================================
MSG: iiwa_msgs/JointImpedanceControlMode
# Stiffness values in [Nm/rad]. Stiffness values must be >= 0. 
JointQuantity joint_stiffness

# Damping values. Damping values must be between 0 and 1. 
JointQuantity joint_damping

================================================================================
MSG: iiwa_msgs/JointQuantity
float32 a1
float32 a2
float32 a3
float32 a4
float32 a5
float32 a6
float32 a7
================================================================================
MSG: iiwa_msgs/CartesianImpedanceControlMode

# Stiffness values [x, y, z, a, b, c] for the cartesian impedance, x, y, z in [N/m], a, b, c in [Nm/rad]. 
# Precondition: 0.0 <= x, y, z <= 5000.0 and 0.0 <= a, b, c <= 300.0. 
CartesianQuantity cartesian_stiffness

# Dimensionless damping values for the cartesian impedance control, for all degrees of freedom : [x, y, z, a, b, c].
# Precondition: 0.1 <= x, y, z, a, b, c <= 1.0. 
CartesianQuantity cartesian_damping

# The stiffness value for null space [Nm/rad]. 
# Precondition: 0.0 <= value. 
float64 nullspace_stiffness

# The damping parameter for null space [Nm*s/rad]. 
# Precondition: value >= 0.3 and value <= 1.0. - A good damping value is 0.7. 
float64 nullspace_damping
================================================================================
MSG: iiwa_msgs/CartesianQuantity
float32 x
float32 y
float32 z
float32 a
float32 b
float32 c
================================================================================
MSG: iiwa_msgs/DesiredForceControlMode
# The degree of freedom on which the desired force
int32 cartesian_dof

# The value of the desired force. In [N].
float64 desired_force

# The value of the stiffness. In [N/m].
float64 desired_stiffness
================================================================================
MSG: iiwa_msgs/SinePatternControlMode
# The degree of freedom for performing the sine oscillation.
int32 cartesian_dof

# The value of the frequency for the sine oscillation [Hz].
float64 frequency

# The value of the amplitude. In [N].
float64 amplitude

# The value of the stiffness. In [N/m].
float64 stiffness
================================================================================
MSG: iiwa_msgs/CartesianControlModeLimits
# Sets the maximum cartesian deviation accepted. If the deviation is exceeded a stop condition occurs. 
# [x, y, z] in [mm]. Precondition: value > 0.0.
# [a, b, c] in [rad]. Precondition: value > 0.0.
CartesianQuantity max_path_deviation

# The maximum control force parameter.
# [x, y, z] in [N]. Precondition: value > 0.0.
# [a, b, c] in [Nm]. Precondition: value > 0.0.
CartesianQuantity max_control_force

# Indicates whether a stop condition is fired if the maximum control force is exceeded. 
bool max_control_force_stop

# Maximum Cartesian velocity parameter 
# [x, y, z] in [mm/s]. Precondition: value > 0.0.
# [a, b, c] in [rad/s]. Precondition: value > 0.0.
CartesianQuantity max_cartesian_velocity 
"""
  __slots__ = ['control_mode','joint_impedance','cartesian_impedance','desired_force','sine_pattern','limits']
  _slot_types = ['int32','iiwa_msgs/JointImpedanceControlMode','iiwa_msgs/CartesianImpedanceControlMode','iiwa_msgs/DesiredForceControlMode','iiwa_msgs/SinePatternControlMode','iiwa_msgs/CartesianControlModeLimits']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       control_mode,joint_impedance,cartesian_impedance,desired_force,sine_pattern,limits

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ConfigureControlModeRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.control_mode is None:
        self.control_mode = 0
      if self.joint_impedance is None:
        self.joint_impedance = iiwa_msgs.msg.JointImpedanceControlMode()
      if self.cartesian_impedance is None:
        self.cartesian_impedance = iiwa_msgs.msg.CartesianImpedanceControlMode()
      if self.desired_force is None:
        self.desired_force = iiwa_msgs.msg.DesiredForceControlMode()
      if self.sine_pattern is None:
        self.sine_pattern = iiwa_msgs.msg.SinePatternControlMode()
      if self.limits is None:
        self.limits = iiwa_msgs.msg.CartesianControlModeLimits()
    else:
      self.control_mode = 0
      self.joint_impedance = iiwa_msgs.msg.JointImpedanceControlMode()
      self.cartesian_impedance = iiwa_msgs.msg.CartesianImpedanceControlMode()
      self.desired_force = iiwa_msgs.msg.DesiredForceControlMode()
      self.sine_pattern = iiwa_msgs.msg.SinePatternControlMode()
      self.limits = iiwa_msgs.msg.CartesianControlModeLimits()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_i26f2di2di3d12fB6f().pack(_x.control_mode, _x.joint_impedance.joint_stiffness.a1, _x.joint_impedance.joint_stiffness.a2, _x.joint_impedance.joint_stiffness.a3, _x.joint_impedance.joint_stiffness.a4, _x.joint_impedance.joint_stiffness.a5, _x.joint_impedance.joint_stiffness.a6, _x.joint_impedance.joint_stiffness.a7, _x.joint_impedance.joint_damping.a1, _x.joint_impedance.joint_damping.a2, _x.joint_impedance.joint_damping.a3, _x.joint_impedance.joint_damping.a4, _x.joint_impedance.joint_damping.a5, _x.joint_impedance.joint_damping.a6, _x.joint_impedance.joint_damping.a7, _x.cartesian_impedance.cartesian_stiffness.x, _x.cartesian_impedance.cartesian_stiffness.y, _x.cartesian_impedance.cartesian_stiffness.z, _x.cartesian_impedance.cartesian_stiffness.a, _x.cartesian_impedance.cartesian_stiffness.b, _x.cartesian_impedance.cartesian_stiffness.c, _x.cartesian_impedance.cartesian_damping.x, _x.cartesian_impedance.cartesian_damping.y, _x.cartesian_impedance.cartesian_damping.z, _x.cartesian_impedance.cartesian_damping.a, _x.cartesian_impedance.cartesian_damping.b, _x.cartesian_impedance.cartesian_damping.c, _x.cartesian_impedance.nullspace_stiffness, _x.cartesian_impedance.nullspace_damping, _x.desired_force.cartesian_dof, _x.desired_force.desired_force, _x.desired_force.desired_stiffness, _x.sine_pattern.cartesian_dof, _x.sine_pattern.frequency, _x.sine_pattern.amplitude, _x.sine_pattern.stiffness, _x.limits.max_path_deviation.x, _x.limits.max_path_deviation.y, _x.limits.max_path_deviation.z, _x.limits.max_path_deviation.a, _x.limits.max_path_deviation.b, _x.limits.max_path_deviation.c, _x.limits.max_control_force.x, _x.limits.max_control_force.y, _x.limits.max_control_force.z, _x.limits.max_control_force.a, _x.limits.max_control_force.b, _x.limits.max_control_force.c, _x.limits.max_control_force_stop, _x.limits.max_cartesian_velocity.x, _x.limits.max_cartesian_velocity.y, _x.limits.max_cartesian_velocity.z, _x.limits.max_cartesian_velocity.a, _x.limits.max_cartesian_velocity.b, _x.limits.max_cartesian_velocity.c))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.joint_impedance is None:
        self.joint_impedance = iiwa_msgs.msg.JointImpedanceControlMode()
      if self.cartesian_impedance is None:
        self.cartesian_impedance = iiwa_msgs.msg.CartesianImpedanceControlMode()
      if self.desired_force is None:
        self.desired_force = iiwa_msgs.msg.DesiredForceControlMode()
      if self.sine_pattern is None:
        self.sine_pattern = iiwa_msgs.msg.SinePatternControlMode()
      if self.limits is None:
        self.limits = iiwa_msgs.msg.CartesianControlModeLimits()
      end = 0
      _x = self
      start = end
      end += 245
      (_x.control_mode, _x.joint_impedance.joint_stiffness.a1, _x.joint_impedance.joint_stiffness.a2, _x.joint_impedance.joint_stiffness.a3, _x.joint_impedance.joint_stiffness.a4, _x.joint_impedance.joint_stiffness.a5, _x.joint_impedance.joint_stiffness.a6, _x.joint_impedance.joint_stiffness.a7, _x.joint_impedance.joint_damping.a1, _x.joint_impedance.joint_damping.a2, _x.joint_impedance.joint_damping.a3, _x.joint_impedance.joint_damping.a4, _x.joint_impedance.joint_damping.a5, _x.joint_impedance.joint_damping.a6, _x.joint_impedance.joint_damping.a7, _x.cartesian_impedance.cartesian_stiffness.x, _x.cartesian_impedance.cartesian_stiffness.y, _x.cartesian_impedance.cartesian_stiffness.z, _x.cartesian_impedance.cartesian_stiffness.a, _x.cartesian_impedance.cartesian_stiffness.b, _x.cartesian_impedance.cartesian_stiffness.c, _x.cartesian_impedance.cartesian_damping.x, _x.cartesian_impedance.cartesian_damping.y, _x.cartesian_impedance.cartesian_damping.z, _x.cartesian_impedance.cartesian_damping.a, _x.cartesian_impedance.cartesian_damping.b, _x.cartesian_impedance.cartesian_damping.c, _x.cartesian_impedance.nullspace_stiffness, _x.cartesian_impedance.nullspace_damping, _x.desired_force.cartesian_dof, _x.desired_force.desired_force, _x.desired_force.desired_stiffness, _x.sine_pattern.cartesian_dof, _x.sine_pattern.frequency, _x.sine_pattern.amplitude, _x.sine_pattern.stiffness, _x.limits.max_path_deviation.x, _x.limits.max_path_deviation.y, _x.limits.max_path_deviation.z, _x.limits.max_path_deviation.a, _x.limits.max_path_deviation.b, _x.limits.max_path_deviation.c, _x.limits.max_control_force.x, _x.limits.max_control_force.y, _x.limits.max_control_force.z, _x.limits.max_control_force.a, _x.limits.max_control_force.b, _x.limits.max_control_force.c, _x.limits.max_control_force_stop, _x.limits.max_cartesian_velocity.x, _x.limits.max_cartesian_velocity.y, _x.limits.max_cartesian_velocity.z, _x.limits.max_cartesian_velocity.a, _x.limits.max_cartesian_velocity.b, _x.limits.max_cartesian_velocity.c,) = _get_struct_i26f2di2di3d12fB6f().unpack(str[start:end])
      self.limits.max_control_force_stop = bool(self.limits.max_control_force_stop)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_i26f2di2di3d12fB6f().pack(_x.control_mode, _x.joint_impedance.joint_stiffness.a1, _x.joint_impedance.joint_stiffness.a2, _x.joint_impedance.joint_stiffness.a3, _x.joint_impedance.joint_stiffness.a4, _x.joint_impedance.joint_stiffness.a5, _x.joint_impedance.joint_stiffness.a6, _x.joint_impedance.joint_stiffness.a7, _x.joint_impedance.joint_damping.a1, _x.joint_impedance.joint_damping.a2, _x.joint_impedance.joint_damping.a3, _x.joint_impedance.joint_damping.a4, _x.joint_impedance.joint_damping.a5, _x.joint_impedance.joint_damping.a6, _x.joint_impedance.joint_damping.a7, _x.cartesian_impedance.cartesian_stiffness.x, _x.cartesian_impedance.cartesian_stiffness.y, _x.cartesian_impedance.cartesian_stiffness.z, _x.cartesian_impedance.cartesian_stiffness.a, _x.cartesian_impedance.cartesian_stiffness.b, _x.cartesian_impedance.cartesian_stiffness.c, _x.cartesian_impedance.cartesian_damping.x, _x.cartesian_impedance.cartesian_damping.y, _x.cartesian_impedance.cartesian_damping.z, _x.cartesian_impedance.cartesian_damping.a, _x.cartesian_impedance.cartesian_damping.b, _x.cartesian_impedance.cartesian_damping.c, _x.cartesian_impedance.nullspace_stiffness, _x.cartesian_impedance.nullspace_damping, _x.desired_force.cartesian_dof, _x.desired_force.desired_force, _x.desired_force.desired_stiffness, _x.sine_pattern.cartesian_dof, _x.sine_pattern.frequency, _x.sine_pattern.amplitude, _x.sine_pattern.stiffness, _x.limits.max_path_deviation.x, _x.limits.max_path_deviation.y, _x.limits.max_path_deviation.z, _x.limits.max_path_deviation.a, _x.limits.max_path_deviation.b, _x.limits.max_path_deviation.c, _x.limits.max_control_force.x, _x.limits.max_control_force.y, _x.limits.max_control_force.z, _x.limits.max_control_force.a, _x.limits.max_control_force.b, _x.limits.max_control_force.c, _x.limits.max_control_force_stop, _x.limits.max_cartesian_velocity.x, _x.limits.max_cartesian_velocity.y, _x.limits.max_cartesian_velocity.z, _x.limits.max_cartesian_velocity.a, _x.limits.max_cartesian_velocity.b, _x.limits.max_cartesian_velocity.c))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.joint_impedance is None:
        self.joint_impedance = iiwa_msgs.msg.JointImpedanceControlMode()
      if self.cartesian_impedance is None:
        self.cartesian_impedance = iiwa_msgs.msg.CartesianImpedanceControlMode()
      if self.desired_force is None:
        self.desired_force = iiwa_msgs.msg.DesiredForceControlMode()
      if self.sine_pattern is None:
        self.sine_pattern = iiwa_msgs.msg.SinePatternControlMode()
      if self.limits is None:
        self.limits = iiwa_msgs.msg.CartesianControlModeLimits()
      end = 0
      _x = self
      start = end
      end += 245
      (_x.control_mode, _x.joint_impedance.joint_stiffness.a1, _x.joint_impedance.joint_stiffness.a2, _x.joint_impedance.joint_stiffness.a3, _x.joint_impedance.joint_stiffness.a4, _x.joint_impedance.joint_stiffness.a5, _x.joint_impedance.joint_stiffness.a6, _x.joint_impedance.joint_stiffness.a7, _x.joint_impedance.joint_damping.a1, _x.joint_impedance.joint_damping.a2, _x.joint_impedance.joint_damping.a3, _x.joint_impedance.joint_damping.a4, _x.joint_impedance.joint_damping.a5, _x.joint_impedance.joint_damping.a6, _x.joint_impedance.joint_damping.a7, _x.cartesian_impedance.cartesian_stiffness.x, _x.cartesian_impedance.cartesian_stiffness.y, _x.cartesian_impedance.cartesian_stiffness.z, _x.cartesian_impedance.cartesian_stiffness.a, _x.cartesian_impedance.cartesian_stiffness.b, _x.cartesian_impedance.cartesian_stiffness.c, _x.cartesian_impedance.cartesian_damping.x, _x.cartesian_impedance.cartesian_damping.y, _x.cartesian_impedance.cartesian_damping.z, _x.cartesian_impedance.cartesian_damping.a, _x.cartesian_impedance.cartesian_damping.b, _x.cartesian_impedance.cartesian_damping.c, _x.cartesian_impedance.nullspace_stiffness, _x.cartesian_impedance.nullspace_damping, _x.desired_force.cartesian_dof, _x.desired_force.desired_force, _x.desired_force.desired_stiffness, _x.sine_pattern.cartesian_dof, _x.sine_pattern.frequency, _x.sine_pattern.amplitude, _x.sine_pattern.stiffness, _x.limits.max_path_deviation.x, _x.limits.max_path_deviation.y, _x.limits.max_path_deviation.z, _x.limits.max_path_deviation.a, _x.limits.max_path_deviation.b, _x.limits.max_path_deviation.c, _x.limits.max_control_force.x, _x.limits.max_control_force.y, _x.limits.max_control_force.z, _x.limits.max_control_force.a, _x.limits.max_control_force.b, _x.limits.max_control_force.c, _x.limits.max_control_force_stop, _x.limits.max_cartesian_velocity.x, _x.limits.max_cartesian_velocity.y, _x.limits.max_cartesian_velocity.z, _x.limits.max_cartesian_velocity.a, _x.limits.max_cartesian_velocity.b, _x.limits.max_cartesian_velocity.c,) = _get_struct_i26f2di2di3d12fB6f().unpack(str[start:end])
      self.limits.max_control_force_stop = bool(self.limits.max_control_force_stop)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_i26f2di2di3d12fB6f = None
def _get_struct_i26f2di2di3d12fB6f():
    global _struct_i26f2di2di3d12fB6f
    if _struct_i26f2di2di3d12fB6f is None:
        _struct_i26f2di2di3d12fB6f = struct.Struct("<i26f2di2di3d12fB6f")
    return _struct_i26f2di2di3d12fB6f
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from iiwa_msgs/ConfigureControlModeResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ConfigureControlModeResponse(genpy.Message):
  _md5sum = "45872d25d65c97743cc71afc6d4e884d"
  _type = "iiwa_msgs/ConfigureControlModeResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool success
string error
"""
  __slots__ = ['success','error']
  _slot_types = ['bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success,error

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ConfigureControlModeResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
      if self.error is None:
        self.error = ''
    else:
      self.success = False
      self.error = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
      _x = self.error
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.error = str[start:end].decode('utf-8')
      else:
        self.error = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
      _x = self.error
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.error = str[start:end].decode('utf-8')
      else:
        self.error = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class ConfigureControlMode(object):
  _type          = 'iiwa_msgs/ConfigureControlMode'
  _md5sum = '680a54772ae74cfe325dd171700c3d78'
  _request_class  = ConfigureControlModeRequest
  _response_class = ConfigureControlModeResponse
