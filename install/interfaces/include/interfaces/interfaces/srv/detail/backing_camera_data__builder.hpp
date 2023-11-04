// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/BackingCameraData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__BACKING_CAMERA_DATA__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__BACKING_CAMERA_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/backing_camera_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::BackingCameraData_Request>()
{
  return ::interfaces::srv::BackingCameraData_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_BackingCameraData_Response_gap
{
public:
  explicit Init_BackingCameraData_Response_gap(::interfaces::srv::BackingCameraData_Response & msg)
  : msg_(msg)
  {}
  ::interfaces::srv::BackingCameraData_Response gap(::interfaces::srv::BackingCameraData_Response::_gap_type arg)
  {
    msg_.gap = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::BackingCameraData_Response msg_;
};

class Init_BackingCameraData_Response_degree
{
public:
  explicit Init_BackingCameraData_Response_degree(::interfaces::srv::BackingCameraData_Response & msg)
  : msg_(msg)
  {}
  Init_BackingCameraData_Response_gap degree(::interfaces::srv::BackingCameraData_Response::_degree_type arg)
  {
    msg_.degree = std::move(arg);
    return Init_BackingCameraData_Response_gap(msg_);
  }

private:
  ::interfaces::srv::BackingCameraData_Response msg_;
};

class Init_BackingCameraData_Response_pos
{
public:
  Init_BackingCameraData_Response_pos()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BackingCameraData_Response_degree pos(::interfaces::srv::BackingCameraData_Response::_pos_type arg)
  {
    msg_.pos = std::move(arg);
    return Init_BackingCameraData_Response_degree(msg_);
  }

private:
  ::interfaces::srv::BackingCameraData_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::BackingCameraData_Response>()
{
  return interfaces::srv::builder::Init_BackingCameraData_Response_pos();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__BACKING_CAMERA_DATA__BUILDER_HPP_
