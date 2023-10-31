// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/GoingCameraData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__GOING_CAMERA_DATA__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__GOING_CAMERA_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/going_camera_data__struct.hpp"
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
auto build<::interfaces::srv::GoingCameraData_Request>()
{
  return ::interfaces::srv::GoingCameraData_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_GoingCameraData_Response_gap
{
public:
  Init_GoingCameraData_Response_gap()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::GoingCameraData_Response gap(::interfaces::srv::GoingCameraData_Response::_gap_type arg)
  {
    msg_.gap = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::GoingCameraData_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::GoingCameraData_Response>()
{
  return interfaces::srv::builder::Init_GoingCameraData_Response_gap();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__GOING_CAMERA_DATA__BUILDER_HPP_
