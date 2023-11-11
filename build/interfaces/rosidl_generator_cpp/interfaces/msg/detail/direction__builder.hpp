// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Direction.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__DIRECTION__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__DIRECTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/direction__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Direction_direction
{
public:
  Init_Direction_direction()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::msg::Direction direction(::interfaces::msg::Direction::_direction_type arg)
  {
    msg_.direction = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Direction msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Direction>()
{
  return interfaces::msg::builder::Init_Direction_direction();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__DIRECTION__BUILDER_HPP_
