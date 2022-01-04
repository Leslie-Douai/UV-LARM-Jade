------
Installer ROS Environnment sur Ubuntu
http://wiki.ros.org/noetic/Installation/Ubuntu
------

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

sudo apt update

sudo apt install ros-noetic-desktop-full

apt search ros-noetic

source /opt/ros/noetic/setup.bash

echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc

---------
dependencies
---------

sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

sudo apt install python3-rosdep

sudo rosdep init
rosdep update
---------

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
