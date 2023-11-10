// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/Back.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__BACK__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__BACK__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces__msg__Back __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__Back __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Back_
{
  using Type = Back_<ContainerAllocator>;

  explicit Back_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pos = "";
      this->degree = 0.0;
      this->diff = 0ll;
    }
  }

  explicit Back_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pos(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pos = "";
      this->degree = 0.0;
      this->diff = 0ll;
    }
  }

  // field types and members
  using _pos_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _pos_type pos;
  using _degree_type =
    double;
  _degree_type degree;
  using _diff_type =
    int64_t;
  _diff_type diff;

  // setters for named parameter idiom
  Type & set__pos(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->pos = _arg;
    return *this;
  }
  Type & set__degree(
    const double & _arg)
  {
    this->degree = _arg;
    return *this;
  }
  Type & set__diff(
    const int64_t & _arg)
  {
    this->diff = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::Back_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::Back_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::Back_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::Back_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Back_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Back_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Back_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Back_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::Back_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::Back_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__Back
    std::shared_ptr<interfaces::msg::Back_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__Back
    std::shared_ptr<interfaces::msg::Back_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Back_ & other) const
  {
    if (this->pos != other.pos) {
      return false;
    }
    if (this->degree != other.degree) {
      return false;
    }
    if (this->diff != other.diff) {
      return false;
    }
    return true;
  }
  bool operator!=(const Back_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Back_

// alias to use template instance with default allocator
using Back =
  interfaces::msg::Back_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__BACK__STRUCT_HPP_
