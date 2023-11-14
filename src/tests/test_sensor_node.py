from threading import Event
from threading import Thread
import launch
import launch_pytest
import launch_ros
import pytest
import rclpy
from rclpy.node import Node
from interfaces.msg import Distance


@launch_pytest.fixture
def generate_test_description():
    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package="sensor_node", executable="sensor_node"
            ),
        ]
    )


@pytest.mark.launch(fixture=generate_test_description)
def test_check_if_msgs_published():
    rclpy.init()
    try:
        node = MakeTestNode("test_node")
        node.start_subscriber()
        msgs_received_flag = node.msg_event_object.wait(timeout=5.0)
        assert msgs_received_flag, "Did not receive msgs !"
        assert isinstance(node.top_left, float)
        assert isinstance(node.top_right, float)
        assert isinstance(node.bottom_left, float)
        assert isinstance(node.bottom_right, float)
    finally:
        rclpy.shutdown()


class MakeTestNode(Node):
    def __init__(self, name="test_node"):
        super().__init__(name)
        self.msg_event_object = Event()

    def start_subscriber(self):
        self.subscription = self.create_subscription(
            Distance, "sensor_node", self.subscriber_callback, 10
        )

        self.ros_spin_thread = Thread(
            target=lambda node: rclpy.spin(node), args=(self,)
        )
        self.ros_spin_thread.start()

    def subscriber_callback(self, msg):
        self.msg_event_object.set()
        self.top_left = msg.top_left
        self.top_right = msg.top_right
        self.bottom_left = msg.bottom_left
        self.bottom_right = msg.bottom_right
