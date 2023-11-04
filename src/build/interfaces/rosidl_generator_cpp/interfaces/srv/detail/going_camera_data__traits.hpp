// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/GoingCameraData.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__GOING_CAMERA_DATA__TRAITS_HPP_
#define INTERFACES__SRV__DETAIL__GOING_CAMERA_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "interfaces/srv/detail/going_camera_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const GoingCameraData_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GoingCameraData_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GoingCameraData_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::srv::GoingCameraData_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::GoingCameraData_Request & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::GoingCameraData_Request>()
{
  return "interfaces::srv::GoingCameraData_Request";
}

template<>
inline const char * name<interfaces::srv::GoingCameraData_Request>()
{
  return "interfaces/srv/GoingCameraData_Request";
}

template<>
struct has_fixed_size<interfaces::srv::GoingCameraData_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::GoingCameraData_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::GoingCameraData_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const GoingCameraData_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: gap
  {
    out << "gap: ";
    rosidl_generator_traits::value_to_yaml(msg.gap, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GoingCameraData_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: gap
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gap: ";
    rosidl_generator_traits::value_to_yaml(msg.gap, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GoingCameraData_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace interfaces

namespace rosidl_generator_traits
{

[[deprecated("use interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const interfaces::srv::GoingCameraData_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const interfaces::srv::GoingCameraData_Response & msg)
{
  return interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<interfaces::srv::GoingCameraData_Response>()
{
  return "interfaces::srv::GoingCameraData_Response";
}

template<>
inline const char * name<interfaces::srv::GoingCameraData_Response>()
{
  return "interfaces/srv/GoingCameraData_Response";
}

template<>
struct has_fixed_size<interfaces::srv::GoingCameraData_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::GoingCameraData_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<interfaces::srv::GoingCameraData_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::GoingCameraData>()
{
  return "interfaces::srv::GoingCameraData";
}

template<>
inline const char * name<interfaces::srv::GoingCameraData>()
{
  return "interfaces/srv/GoingCameraData";
}

template<>
struct has_fixed_size<interfaces::srv::GoingCameraData>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::GoingCameraData_Request>::value &&
    has_fixed_size<interfaces::srv::GoingCameraData_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::GoingCameraData>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::GoingCameraData_Request>::value &&
    has_bounded_size<interfaces::srv::GoingCameraData_Response>::value
  >
{
};

template<>
struct is_service<interfaces::srv::GoingCameraData>
  : std::true_type
{
};

template<>
struct is_service_request<interfaces::srv::GoingCameraData_Request>
  : std::true_type
{
};

template<>
struct is_service_response<interfaces::srv::GoingCameraData_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__DETAIL__GOING_CAMERA_DATA__TRAITS_HPP_
