// Generated by gencpp from file iiwa_msgs/JointQuantity.msg
// DO NOT EDIT!


#ifndef IIWA_MSGS_MESSAGE_JOINTQUANTITY_H
#define IIWA_MSGS_MESSAGE_JOINTQUANTITY_H


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
struct JointQuantity_
{
  typedef JointQuantity_<ContainerAllocator> Type;

  JointQuantity_()
    : a1(0.0)
    , a2(0.0)
    , a3(0.0)
    , a4(0.0)
    , a5(0.0)
    , a6(0.0)
    , a7(0.0)  {
    }
  JointQuantity_(const ContainerAllocator& _alloc)
    : a1(0.0)
    , a2(0.0)
    , a3(0.0)
    , a4(0.0)
    , a5(0.0)
    , a6(0.0)
    , a7(0.0)  {
  (void)_alloc;
    }



   typedef float _a1_type;
  _a1_type a1;

   typedef float _a2_type;
  _a2_type a2;

   typedef float _a3_type;
  _a3_type a3;

   typedef float _a4_type;
  _a4_type a4;

   typedef float _a5_type;
  _a5_type a5;

   typedef float _a6_type;
  _a6_type a6;

   typedef float _a7_type;
  _a7_type a7;





  typedef boost::shared_ptr< ::iiwa_msgs::JointQuantity_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::iiwa_msgs::JointQuantity_<ContainerAllocator> const> ConstPtr;

}; // struct JointQuantity_

typedef ::iiwa_msgs::JointQuantity_<std::allocator<void> > JointQuantity;

typedef boost::shared_ptr< ::iiwa_msgs::JointQuantity > JointQuantityPtr;
typedef boost::shared_ptr< ::iiwa_msgs::JointQuantity const> JointQuantityConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::iiwa_msgs::JointQuantity_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::iiwa_msgs::JointQuantity_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::iiwa_msgs::JointQuantity_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::iiwa_msgs::JointQuantity_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::iiwa_msgs::JointQuantity_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::iiwa_msgs::JointQuantity_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iiwa_msgs::JointQuantity_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::iiwa_msgs::JointQuantity_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::iiwa_msgs::JointQuantity_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b9f90cf50b6e4af396f731df7da11689";
  }

  static const char* value(const ::iiwa_msgs::JointQuantity_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb9f90cf50b6e4af3ULL;
  static const uint64_t static_value2 = 0x96f731df7da11689ULL;
};

template<class ContainerAllocator>
struct DataType< ::iiwa_msgs::JointQuantity_<ContainerAllocator> >
{
  static const char* value()
  {
    return "iiwa_msgs/JointQuantity";
  }

  static const char* value(const ::iiwa_msgs::JointQuantity_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::iiwa_msgs::JointQuantity_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 a1\n"
"float32 a2\n"
"float32 a3\n"
"float32 a4\n"
"float32 a5\n"
"float32 a6\n"
"float32 a7\n"
;
  }

  static const char* value(const ::iiwa_msgs::JointQuantity_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::iiwa_msgs::JointQuantity_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.a1);
      stream.next(m.a2);
      stream.next(m.a3);
      stream.next(m.a4);
      stream.next(m.a5);
      stream.next(m.a6);
      stream.next(m.a7);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct JointQuantity_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::iiwa_msgs::JointQuantity_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::iiwa_msgs::JointQuantity_<ContainerAllocator>& v)
  {
    s << indent << "a1: ";
    Printer<float>::stream(s, indent + "  ", v.a1);
    s << indent << "a2: ";
    Printer<float>::stream(s, indent + "  ", v.a2);
    s << indent << "a3: ";
    Printer<float>::stream(s, indent + "  ", v.a3);
    s << indent << "a4: ";
    Printer<float>::stream(s, indent + "  ", v.a4);
    s << indent << "a5: ";
    Printer<float>::stream(s, indent + "  ", v.a5);
    s << indent << "a6: ";
    Printer<float>::stream(s, indent + "  ", v.a6);
    s << indent << "a7: ";
    Printer<float>::stream(s, indent + "  ", v.a7);
  }
};

} // namespace message_operations
} // namespace ros

#endif // IIWA_MSGS_MESSAGE_JOINTQUANTITY_H
