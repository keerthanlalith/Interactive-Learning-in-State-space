// Generated by gencpp from file iiwa_msgs/DOF.msg
// DO NOT EDIT!


#ifndef IIWA_MSGS_MESSAGE_DOF_H
#define IIWA_MSGS_MESSAGE_DOF_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace iiwa_msgs
{
template <class ContainerAllocator>
struct DOF_
{
  typedef DOF_<ContainerAllocator> Type;

  DOF_()
    {
    }
  DOF_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }





  enum {
    X = 1,
    Y = 2,
    Z = 3,
    A = 4,
    B = 5,
    C = 6,
    ROT = 7,
    TRANSL = 8,
    ALL = 9,
  };


  typedef boost::shared_ptr< ::iiwa_msgs::DOF_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iiwa_msgs::DOF_<ContainerAllocator> const> ConstPtr;

}; // struct DOF_

typedef ::iiwa_msgs::DOF_<std::allocator<void> > DOF;

typedef boost::shared_ptr< ::iiwa_msgs::DOF > DOFPtr;
typedef boost::shared_ptr< ::iiwa_msgs::DOF const> DOFConstPtr;

// constants requiring out of line definition

   

   

   

   

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::iiwa_msgs::DOF_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::iiwa_msgs::DOF_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace iiwa_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/melodic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'iiwa_msgs': ['/home/snehal/Desktop/Thesis/IfO/KUKA_Task/ros_ws/src/iiwa_stack/iiwa_msgs/msg', '/home/snehal/Desktop/Thesis/IfO/KUKA_Task/ros_ws/devel/share/iiwa_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::iiwa_msgs::DOF_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::iiwa_msgs::DOF_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::iiwa_msgs::DOF_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::iiwa_msgs::DOF_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iiwa_msgs::DOF_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iiwa_msgs::DOF_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::iiwa_msgs::DOF_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c1a133d87080cb4a84e23090e4a06363";
  }

  static const char* value(const ::iiwa_msgs::DOF_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc1a133d87080cb4aULL;
  static const uint64_t static_value2 = 0x84e23090e4a06363ULL;
};

template<class ContainerAllocator>
struct DataType< ::iiwa_msgs::DOF_<ContainerAllocator> >
{
  static const char* value()
  {
    return "iiwa_msgs/DOF";
  }

  static const char* value(const ::iiwa_msgs::DOF_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::iiwa_msgs::DOF_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 X = 1\n"
"int32 Y = 2\n"
"int32 Z = 3\n"
"int32 A = 4\n"
"int32 B = 5\n"
"int32 C = 6\n"
"int32 ROT = 7\n"
"int32 TRANSL = 8\n"
"int32 ALL = 9\n"
;
  }

  static const char* value(const ::iiwa_msgs::DOF_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::iiwa_msgs::DOF_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DOF_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iiwa_msgs::DOF_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::iiwa_msgs::DOF_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // IIWA_MSGS_MESSAGE_DOF_H
