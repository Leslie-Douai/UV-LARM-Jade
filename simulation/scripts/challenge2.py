from fonction.py import *

#enveloppe
enveloppe(0.2,0.1)


# Initialize ROS::node
rospy.init_node('move', anonymous=True)

# connect to the topic:
rospy.Subscriber('scan', LaserScan, interpret_scan)

# call the aire_evoluer_robot at a regular frequency:
rospy.Timer( rospy.Duration(0.1), faire_evoluer_robot, oneshot=False )
rospy.spin()
