// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__GOAL__STRUCT_HPP_
#define INTERFACES__MSG__DETAIL__GOAL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces__msg__Goal __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__Goal __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Goal_
{
  using Type = Goal_<ContainerAllocator>;

  explicit Goal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->diff = 0ll;
    }
  }

  explicit Goal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->diff = 0ll;
    }
  }

  // field types and members
  using _diff_type =
    int64_t;
  _diff_type diff;

  // setters for named parameter idiom
  Type & set__diff(
    const int64_t & _arg)
  {
    this->diff = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__Goal
    std::shared_ptr<interfaces::msg::Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__Goal
    std::shared_ptr<interfaces::msg::Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Goal_ & other) const
  {
    if (this->diff != other.diff) {
      return false;
    }
    return true;
  }
  bool operator!=(const Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Goal_

// alias to use template instance with default allocator
using Goal =
  interfaces::msg::Goal_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__GOAL__STRUCT_HPP_
