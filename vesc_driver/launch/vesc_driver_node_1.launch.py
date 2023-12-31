import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    vesc_config = os.path.join(
        get_package_share_directory('vesc_driver'),
        'params',
        'vesc_config_2.yaml'
        )
    return LaunchDescription([
        DeclareLaunchArgument(
            name="config",
            default_value=vesc_config,
            description="VESC yaml configuration file.",
            ),
        Node(
            package='vesc_driver',
            executable='vesc_driver_node',
            name='vesc_driver_node_1',
            parameters=[LaunchConfiguration("config")]
        ),

    ])