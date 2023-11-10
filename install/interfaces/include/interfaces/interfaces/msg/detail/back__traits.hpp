// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/Back.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__DETAIL__BACK__TRAITS_HPP_
#define INTERFACES__MSG__DETAIL__BACK__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/msg/detail/back__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Back & msg,
  std::ostream & out)
{
  out << "{";
  // member: pos
  {
    out << "pos: ";
    rosidl_generator_traits::value_to_yaml(msg.pos, out);
    out << ", ";
  }

  // member: degree
  {
    out << "degree: ";
    rosidl_generator_traits::value_to_yaml(msg.degree, out);
    out << ", ";
  }

  // member: diff
  {
    out << "diff: ";
    rosidl_generator_traits::value_to_yaml(msg.diff, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Back & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pos: ";
    rosidl_generator_traits::value_to_yaml(msg.pos, out);
    out << "\n";
  }

  // member: degree
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "degree: ";
    rosidl_generator_traits::value_to_yaml(msg.degree, out);
    out << "\n";
  }

  // member: diff
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "diff: ";
    rosidl_generator_traits::value_to_yaml(msg.diff, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Back & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::msg::Back & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::msg::Back & msg)
{
  return interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::msg::Back>()
{
  return "interfaces::msg::Back";
}

template<>
inline const char * name<interfaces::msg::Back>()
{
  return "interfaces/msg/Back";
}

template<>
struct has_fixed_size<interfaces::msg::Back>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces::msg::Back>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<interfaces::msg::Back>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__DETAIL__BACK__TRAITS_HPP_
