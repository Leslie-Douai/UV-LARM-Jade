#!/usr/bin/python3
from __future__ import print_function
from os import posix_fadvise
import cv2 as cv
import argparse
import numpy
import math
import rospy, rospkg
import tf
import fonction
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, PoseStamped
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
from cv_bridge import CvBridge, CvBridgeError



class BottleDetection():
	def __init__(self):
		
		self.cascade = cv.CascadeClassifier("/mnt/Secondaire/catkin-ws/src/UV-LARM-Jade/vision/modele/cascade.xml")
		self.tfListener = tf.TransformListener()
		self.markerPublisher = rospy.Publisher('/bottle',Marker, queue_size=10)
		self.camera_width = 1920.0
		self.camera_height = 1080.0
		self.hfov = 64

	def detectAndDisplay(self, frame):
		frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		frame_gray = cv.equalizeHist(frame_gray)	
		color_info = (255, 255, 255)		
		cv.imshow('Capture', frame_gray)
		cv.waitKey(300)
	
		self.cascade.detectMultiScale(frame_gray, scaleFactor=1.10, minNeighbors=3)
		print(self.cascade.detectMultiScale(frame_gray, scaleFactor=1.10, minNeighbors=3))
		'''for (x, y, w, h) in bottles:
			center=(x+(w/2),y+(h/2))
			frame=cv.ellipse(frame,center,(w/2,h/2),(255,0,255),4)
			estimated_pose = self.Pose(x,y, w, h)
			self.position_marqueur(estimated_pose)'''
	
		

	def Pose(self, x, y, w, h):
		distance = 2000
		for row in self.depth_array[y:y+h, x:x+w]:
			for pixel in row:
				if pixel < distance and pixel != 0:
					distance = pixel  
		angle = ((x+w - self.camera_width/2)/(self.camera_width/2))*(self.hfov/2) * math.pi / 180
		estimated_pose = Pose()
		estimated_pose.position.x = distance / 1000 * math.cos(angle) 
		estimated_pose.position.y = distance / 1000 * math.sin(angle)  
		return estimated_pose


	def Coordonnee_odom(self, data: Odometry):
		self.position = data.pose

	def callback_depth(self, data: Image):
		m=1

	def callback_image(self, data: Image):
		bridge = CvBridge()
		try:
			cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
			self.detectAndDisplay(cv_image)
		except Exception as err:
			print("Erreur ", err)

	"""def position_marqueur(self, pose: Pose):
		if len(self.markers_list) == 0:
			pose_marqueur = self.Creation_marqueur(pose)
			self.markerPublisher.publish(pose_marqueur)
			self.markers_list.append(pose_marqueur)"""

	def Creation_marqueur(self, pose: Pose):
		pose_stamped = PoseStamped ()
		pose_stamped.pose = pose
		pose_stamped.header.frame_id = "map"
		pose_stamped = self.tfListener.transformPose("map", pose_stamped)
		marker = Marker()
		marker.type = Marker.CUBE
		marker.action = Marker.ADD
		marker.pose = pose_stamped.pose
		marker.scale.x = 0.5
		marker.scale.y = 0.5
		marker.scale.z = 0.5

		marker.color.r = 0.0
		marker.color.g = 0.0
		marker.color.b = 1.0
		marker.color.a = 1.0



def depth_to_color_image_raw_cb(data: Image):
	global node
	node.callback_depth(data)

def color_image_raw_cb(data: Image):
	global node
	node.callback_image(data)
	
def odom(data: Odometry):
	global node 
	node.Coordonnee_odom(data)




#enveloppe
enveloppe_x = 0.2
enveloppe_y = 0.1

# Initialize ROS::node
rospy.init_node('move', anonymous=True)

# connect to the topic:
print("interpret_scan")
rospy.Subscriber('scan', LaserScan, interpret_scan)

# call the aire_evoluer_robot at a regular frequency:
print("faire_evoluer_robot")
rospy.Timer( rospy.Duration(0.1), faire_evoluer_robot, oneshot=False )
print("Normalement j'apparait")
#spin() enter the program in a infinite loop
print("Start challenge1.py")
rospy.spin()
print("C'est fini le spin est fini")

rospy.init_node('Bottle_Detection', anonymous=True)
node = BottleDetection()
rospy.Subscriber("camera/aligned_depth_to_color/image_raw", Image,depth_to_color_image_raw_cb)
rospy.Subscriber("camera/color/image_raw",Image, color_image_raw_cb)
rospy.Subscriber("/odom", Odometry, odom)
rospy.spin()

