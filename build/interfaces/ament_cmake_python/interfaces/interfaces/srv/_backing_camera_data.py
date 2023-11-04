# generated from rosidl_generator_py/resource/_idl.py.em
# with input from interfaces:srv/BackingCameraData.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BackingCameraData_Request(type):
    """Metaclass of message 'BackingCameraData_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interfaces.srv.BackingCameraData_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__backing_camera_data__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__backing_camera_data__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__backing_camera_data__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__backing_camera_data__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__backing_camera_data__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BackingCameraData_Request(metaclass=Metaclass_BackingCameraData_Request):
    """Message class 'BackingCameraData_Request'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_BackingCameraData_Response(type):
    """Metaclass of message 'BackingCameraData_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interfaces.srv.BackingCameraData_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__backing_camera_data__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__backing_camera_data__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__backing_camera_data__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__backing_camera_data__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__backing_camera_data__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BackingCameraData_Response(metaclass=Metaclass_BackingCameraData_Response):
    """Message class 'BackingCameraData_Response'."""

    __slots__ = [
        '_pos',
        '_degree',
        '_gap',
    ]

    _fields_and_field_types = {
        'pos': 'string',
        'degree': 'double',
        'gap': 'int64',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int64'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.pos = kwargs.get('pos', str())
        self.degree = kwargs.get('degree', float())
        self.gap = kwargs.get('gap', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.pos != other.pos:
            return False
        if self.degree != other.degree:
            return False
        if self.gap != other.gap:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def pos(self):
        """Message field 'pos'."""
        return self._pos

    @pos.setter
    def pos(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'pos' field must be of type 'str'"
        self._pos = value

    @builtins.property
    def degree(self):
        """Message field 'degree'."""
        return self._degree

    @degree.setter
    def degree(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'degree' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'degree' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._degree = value

    @builtins.property
    def gap(self):
        """Message field 'gap'."""
        return self._gap

    @gap.setter
    def gap(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'gap' field must be of type 'int'"
            assert value >= -9223372036854775808 and value < 9223372036854775808, \
                "The 'gap' field must be an integer in [-9223372036854775808, 9223372036854775807]"
        self._gap = value


class Metaclass_BackingCameraData(type):
    """Metaclass of service 'BackingCameraData'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interfaces.srv.BackingCameraData')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__backing_camera_data

            from interfaces.srv import _backing_camera_data
            if _backing_camera_data.Metaclass_BackingCameraData_Request._TYPE_SUPPORT is None:
                _backing_camera_data.Metaclass_BackingCameraData_Request.__import_type_support__()
            if _backing_camera_data.Metaclass_BackingCameraData_Response._TYPE_SUPPORT is None:
                _backing_camera_data.Metaclass_BackingCameraData_Response.__import_type_support__()


class BackingCameraData(metaclass=Metaclass_BackingCameraData):
    from interfaces.srv._backing_camera_data import BackingCameraData_Request as Request
    from interfaces.srv._backing_camera_data import BackingCameraData_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
