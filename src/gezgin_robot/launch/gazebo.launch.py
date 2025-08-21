import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Paketimizin yolunu bul
    pkg_gezgin_robot = get_package_share_directory('gezgin_robot')
    
    # Gazebo'yu başlatmak için gerekli launch dosyasını dahil et
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        # Oluşturduğumuz dünya dosyasını argüman olarak ver
        launch_arguments={'gz_args': '-r ' + os.path.join(pkg_gezgin_robot, 'worlds', 'gezgin_dunyasi.world')}.items(),
    )

    # URDF dosyasını oku ve robot_state_publisher'ı başlat
    robot_description_path = os.path.join(pkg_gezgin_robot, 'urdf', 'gezgin.urdf')
    with open(robot_description_path, 'r') as f:
        robot_description = f.read()

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description, 'use_sim_time': True}]
    )

    # Robotu Gazebo'da spawn etmek için Gz-ROS köprüsünü kullan
    spawn_entity_node = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=['-string', robot_description,
                   '-name', 'gezgin',
                   '-allow_renaming', 'true'],
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher_node,
        spawn_entity_node,
    ])