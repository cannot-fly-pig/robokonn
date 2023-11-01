// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/DistanceSensorData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__DISTANCE_SENSOR_DATA__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__DISTANCE_SENSOR_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/distance_sensor_data__struct.hpp"
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
auto build<::interfaces::srv::DistanceSensorData_Request>()
{
  return ::interfaces::srv::DistanceSensorData_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_DistanceSensorData_Response_distance
{
public:
  Init_DistanceSensorData_Response_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::DistanceSensorData_Response distance(::interfaces::srv::DistanceSensorData_Response::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::DistanceSensorData_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::DistanceSensorData_Response>()
{
  return interfaces::srv::builder::Init_DistanceSensorData_Response_distance();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__DISTANCE_SENSOR_DATA__BUILDER_HPP_
