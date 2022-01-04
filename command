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
Dossier ROS
---------

printenv | grep ROS

#You will need to run this command on every 
#new shell you open to have access to the ROS commands, 
#unless you add this line to your .bashrc.

source /opt/ros/noetic/setup.bash

#create and build a catkin workspace

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make

source devel/setup.bash

echo $ROS_PACKAGE_PATH

-------
Navigating the ROS Filesystem
Noetic + catkin
-------

sudo apt-get install ros-noetic-ros-tutorials

#rospack allows you to get information about packages. 
rospack find [package_name]

rospack find roscpp

#roscd is part of the rosbash suite. It allows you to change directory (cd) directly to a package or a stack
roscd <package-or-stack>[/subdir]

rappel : pwd -> Print Working Directory (shell builtin) 

roscd roscpp
pwd

#Remarque : Note that roscd, like other ROS tools, will only find 
#ROS packages that are within the directories listed in your ROS_PACKAGE_PATH

echo $ROS_PACKAGE_PATH
roscd roscpp/cmake
pwd

#roscd log will take you to the folder where ROS stores log files. Note that if you have not run any 
#ROS programs yet, this will yield an error saying that it does not yet exist.
roscd log

#rosls is part of the rosbash suite. It allows you to ls directly in a package by name rather than by absolute path.
rosls <package-or-stack>[/subdir]


rosls roscpp_tutorials
roscd turtle

-----
Creating a ROS Package
-----
'For a package to be considered a catkin package it must meet a few requirements:

    The package must contain a catkin compliant package.xml file.
        That package.xml file provides meta information about the package. 

    The package must contain a CMakeLists.txt which uses catkin.

        If it is a catkin metapackage it must have the relevant boilerplate CMakeLists.txt file. 
    Each package must have its own folder
        This means no nested packages nor multiple packages sharing the same directory. 

The simplest possible package might have a structure which looks like this:

    my_package/
      CMakeLists.txt
      package.xml
'
catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
#create #create a new package called '<package_name>  which depends on depend1, depend2, and depend3

/!\ rajouter -m user pour que ça marche : the -m option force an author name

catkin_create_pkg -m leslie beginner_tutorials std_msgs rospy roscpp

#build the packages in the catkin workspace
cd ~/catkin_ws
catkin_make

#add the workspace to your ROS environment you need to source the generated setup file
. ~/catkin_ws/devel/setup.bash

#rospack add the workspace to your ROS environment you need to source the generated setup file
rospack depends1 beginner_tutorials 
roscd beginner_tutorials
cat package.xml
rospack depends1 rospy
rospack depends beginner_tutorials

---
La commande à faire h24
---

source /opt/ros/%YOUR_ROS_DISTRO%/setup.bash

----
Remarque pour le github
----

pour recreer l'environnement pkg sur son ordi 
il faut suppr les fichiers cmakelists et package.xml du dossier que l'on veut en pkg puis 
on fait la commande create pkg puis on retourne sur le ws pour faire catkin_make puis on fait 
la cmd . ~/catkin-ws/devel/setup.bash
