#!/usr/bin/python3
import math, rospy, math
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time
import fonction


commandPublisher = rospy.Publisher(
    '/cmd_vel_mux/input/navi',
    Twist, queue_size=10
)

obstacles= []

# Initialize ROS::node
rospy.init_node('move', anonymous=True)

# connect to the topic:
rospy.Subscriber('scan', LaserScan, interpret_scan)

# call the aire_evoluer_robot at a regular frequency:
rospy.Timer( rospy.Duration(0.1), faire_evoluer_robot, oneshot=False )
#spin() enter the program in a infinite loop
rospy.spin()

