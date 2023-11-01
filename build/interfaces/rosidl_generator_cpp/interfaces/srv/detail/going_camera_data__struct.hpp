// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/GoingCameraData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__GOING_CAMERA_DATA__STRUCT_HPP_
#define INTERFACES__SRV__DETAIL__GOING_CAMERA_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__GoingCameraData_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__GoingCameraData_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GoingCameraData_Request_
{
  using Type = GoingCameraData_Request_<ContainerAllocator>;

  explicit GoingCameraData_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit GoingCameraData_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    interfaces::srv::GoingCameraData_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::GoingCameraData_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::GoingCameraData_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::GoingCameraData_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::GoingCameraData_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::GoingCameraData_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::GoingCameraData_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::GoingCameraData_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::GoingCameraData_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::GoingCameraData_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__GoingCameraData_Request
    std::shared_ptr<interfaces::srv::GoingCameraData_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__GoingCameraData_Request
    std::shared_ptr<interfaces::srv::GoingCameraData_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GoingCameraData_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const GoingCameraData_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GoingCameraData_Request_

// alias to use template instance with default allocator
using GoingCameraData_Request =
  interfaces::srv::GoingCameraData_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces


#ifndef _WIN32
# define DEPRECATED__interfaces__srv__GoingCameraData_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__GoingCameraData_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GoingCameraData_Response_
{
  using Type = GoingCameraData_Response_<ContainerAllocator>;

  explicit GoingCameraData_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->gap = 0ll;
    }
  }

  explicit GoingCameraData_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->gap = 0ll;
    }
  }

  // field types and members
  using _gap_type =
    int64_t;
  _gap_type gap;

  // setters for named parameter idiom
  Type & set__gap(
    const int64_t & _arg)
  {
    this->gap = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::GoingCameraData_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::GoingCameraData_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::GoingCameraData_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::GoingCameraData_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::GoingCameraData_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::GoingCameraData_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::GoingCameraData_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::GoingCameraData_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::GoingCameraData_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::GoingCameraData_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__GoingCameraData_Response
    std::shared_ptr<interfaces::srv::GoingCameraData_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__GoingCameraData_Response
    std::shared_ptr<interfaces::srv::GoingCameraData_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GoingCameraData_Response_ & other) const
  {
    if (this->gap != other.gap) {
      return false;
    }
    return true;
  }
  bool operator!=(const GoingCameraData_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GoingCameraData_Response_

// alias to use template instance with default allocator
using GoingCameraData_Response =
  interfaces::srv::GoingCameraData_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct GoingCameraData
{
  using Request = interfaces::srv::GoingCameraData_Request;
  using Response = interfaces::srv::GoingCameraData_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__GOING_CAMERA_DATA__STRUCT_HPP_
