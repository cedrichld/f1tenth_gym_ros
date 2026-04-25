from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    pkg_share = get_package_share_directory('pure_pursuit')
    opp_params = os.path.join(pkg_share, 'config', 'zach_params', 'opp_sim_params.yaml')
    csv_path = os.path.join(pkg_share, 'waypoints', 'old', 'sim', 'sim_waypoints_2_smoothed_profiled.csv')

    return LaunchDescription([
        Node(
            package='pure_pursuit',
            executable='pure_pursuit_node',
            name='opp_pure_pursuit',
            namespace='opp_racecar',
            parameters=[opp_params, {'csv_path': csv_path}],
            remappings=[
                ('/ego_racecar/odom',  '/opp_racecar/odom'),
                ('/drive',             '/opp_drive'),
                ('/waypoint_marker',   '/opp_racecar/waypoint_marker'),
                ('/waypoint_path',     '/opp_racecar/waypoint_path'),
                ('/driven_path',       '/opp_racecar/driven_path'),
            ],
            output='screen',
        )
    ])
