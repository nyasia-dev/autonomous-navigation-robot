import rclpy
from rclpy.node import Node


class StartupNode(Node):

    def __init__(self):
        super().__init__('autonavrobot_startup')

        log = self.get_logger().info

        log("")
        log("=========================================")
        log("      AutoNavRobot Startup System")
        log("=========================================")

        log("✓ Raspberry Pi detected")
        log("✓ ROS 2 Jazzy initialized")

        log("")
        log("Hardware Status")
        log("-----------------------------------------")
        log("[PENDING] Motor Controller")
        log("[PENDING] RPLIDAR")
        log("[PENDING] Battery Monitor")

        log("")
        log("Software Status")
        log("-----------------------------------------")
        log("[PENDING] Navigation Stack")
        log("[PENDING] SLAM")

        log("")
        log("Robot Status: DEVELOPMENT MODE")
        log("=========================================")


def main(args=None):
    rclpy.init(args=args)

    node = StartupNode()

    rclpy.spin_once(node, timeout_sec=1)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()