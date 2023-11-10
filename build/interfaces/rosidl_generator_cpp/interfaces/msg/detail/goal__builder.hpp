// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Goal.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__GOAL__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__GOAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/goal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Goal_diff
{
public:
  Init_Goal_diff()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::msg::Goal diff(::interfaces::msg::Goal::_diff_type arg)
  {
    msg_.diff = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Goal msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Goal>()
{
  return interfaces::msg::builder::Init_Goal_diff();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__GOAL__BUILDER_HPP_
