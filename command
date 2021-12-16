printenv | grep ROS
source /opt/ros/noetic/setup.bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH
sudo apt-get install ros-<distro>-ros-tutorials
rospack find [package_name]
rospack find roscpp
roscd <package-or-stack>[/subdir]
roscd roscpp
pwd
echo $ROS_PACKAGE_PATH
roscd roscpp/cmake
 pwd
 
roscd log
rosls <package-or-stack>[/subdir]
rosls roscpp_tutorials
roscd turtle

catkin_create_pkg -m leslie beginner_tutorials std_msgs rospy roscpp
cd ~/catkin_ws
catkin_make

$ . ~/catkin_ws/devel/setup.bash
rospack depends1 beginner_tutorials 
roscd beginner_tutorials
cat package.xml
rospack depends1 rospy
rospack depends beginner_tutorials

source /opt/ros/%YOUR_ROS_DISTRO%/setup.bash

pour recreer l'environnement pkg sur son ordi 
il faut suppr les fichiers cmakelists et package.xml du dossier que l'on veut en pkg puis 
on fait la commande create pkg puis on retourne sur le ws pour faire catkin_make puis on fait 
la cmd . ~/catkin-ws/devel/setup.bash
