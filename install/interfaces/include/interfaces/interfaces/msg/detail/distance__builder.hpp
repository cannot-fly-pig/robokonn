// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Distance.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__DISTANCE__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__DISTANCE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/distance__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Distance_distance
{
public:
  Init_Distance_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::msg::Distance distance(::interfaces::msg::Distance::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Distance msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Distance>()
{
  return interfaces::msg::builder::Init_Distance_distance();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__DISTANCE__BUILDER_HPP_
