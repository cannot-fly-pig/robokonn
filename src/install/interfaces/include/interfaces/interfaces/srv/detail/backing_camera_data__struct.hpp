// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/BackingCameraData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__BACKING_CAMERA_DATA__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__BACKING_CAMERA_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__BackingCameraData_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__BackingCameraData_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct BackingCameraData_Request_
{
  using Type = BackingCameraData_Request_<ContainerAllocator>;

  explicit BackingCameraData_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit BackingCameraData_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::BackingCameraData_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::BackingCameraData_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::BackingCameraData_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::BackingCameraData_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::BackingCameraData_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::BackingCameraData_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::BackingCameraData_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::BackingCameraData_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::BackingCameraData_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::BackingCameraData_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__BackingCameraData_Request
    std::shared_ptr<interfaces::srv::BackingCameraData_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__BackingCameraData_Request
    std::shared_ptr<interfaces::srv::BackingCameraData_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BackingCameraData_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const BackingCameraData_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BackingCameraData_Request_

// alias to use template instance with default allocator
using BackingCameraData_Request =
  interfaces::srv::BackingCameraData_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__BackingCameraData_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__BackingCameraData_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct BackingCameraData_Response_
{
  using Type = BackingCameraData_Response_<ContainerAllocator>;

  explicit BackingCameraData_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pos = "";
      this->degree = 0.0;
      this->gap = 0ll;
    }
  }

  explicit BackingCameraData_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pos(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->pos = "";
      this->degree = 0.0;
      this->gap = 0ll;
    }
  }

  // field types and members
  using _pos_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _pos_type pos;
  using _degree_type =
    double;
  _degree_type degree;
  using _gap_type =
    int64_t;
  _gap_type gap;

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
  Type & set__gap(
    const int64_t & _arg)
  {
    this->gap = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::BackingCameraData_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::BackingCameraData_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::BackingCameraData_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::BackingCameraData_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::BackingCameraData_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::BackingCameraData_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::BackingCameraData_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::BackingCameraData_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::BackingCameraData_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::BackingCameraData_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__BackingCameraData_Response
    std::shared_ptr<interfaces::srv::BackingCameraData_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__BackingCameraData_Response
    std::shared_ptr<interfaces::srv::BackingCameraData_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BackingCameraData_Response_ & other) const
  {
    if (this->pos != other.pos) {
      return false;
    }
    if (this->degree != other.degree) {
      return false;
    }
    if (this->gap != other.gap) {
      return false;
    }
    return true;
  }
  bool operator!=(const BackingCameraData_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BackingCameraData_Response_

// alias to use template instance with default allocator
using BackingCameraData_Response =
  interfaces::srv::BackingCameraData_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct BackingCameraData
{
  using Request = interfaces::srv::BackingCameraData_Request;
  using Response = interfaces::srv::BackingCameraData_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__BACKING_CAMERA_DATA__STRUCT_HPP_
