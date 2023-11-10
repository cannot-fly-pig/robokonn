// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:msg/Back.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__BACK__BUILDER_HPP_
#define INTERFACES__MSG__DETAIL__BACK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/msg/detail/back__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace msg
{

namespace builder
{

class Init_Back_diff
{
public:
  explicit Init_Back_diff(::interfaces::msg::Back & msg)
  : msg_(msg)
  {}
  ::interfaces::msg::Back diff(::interfaces::msg::Back::_diff_type arg)
  {
    msg_.diff = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::msg::Back msg_;
};

class Init_Back_degree
{
public:
  explicit Init_Back_degree(::interfaces::msg::Back & msg)
  : msg_(msg)
  {}
  Init_Back_diff degree(::interfaces::msg::Back::_degree_type arg)
  {
    msg_.degree = std::move(arg);
    return Init_Back_diff(msg_);
  }

private:
  ::interfaces::msg::Back msg_;
};

class Init_Back_pos
{
public:
  Init_Back_pos()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Back_degree pos(::interfaces::msg::Back::_pos_type arg)
  {
    msg_.pos = std::move(arg);
    return Init_Back_degree(msg_);
  }

private:
  ::interfaces::msg::Back msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::msg::Back>()
{
  return interfaces::msg::builder::Init_Back_pos();
}

}  // namespace interfaces

#endif  // INTERFACES__MSG__DETAIL__BACK__BUILDER_HPP_
