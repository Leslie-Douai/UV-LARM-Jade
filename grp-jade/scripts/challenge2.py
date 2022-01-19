#!/usr/bin/python3
from __future__ import print_function
from os import posix_fadvise
import cv2 as cv
import argparse
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
import numpy
import math
import rospy, rospkg
import tf
from cv_bridge import CvBridge, CvBridgeError
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, PoseStamped

def get_pkg_path():
    rospack = rospkg.RosPack()
    return rospack.get_path('grp-jade')

class Black_Bottle():
	def __init__(self):
		self.cascade = cv.CascadeClassifier(get_pkg_path() + "/scripts/cascade.xml")
		self.tfListener = tf.TransformListener()
		self.publisher = rospy.Publisher('/bottle',Marker, queue_size=10)
		self.map = rospy.Publisher('/map',Marker, queue_size=10)
		self.vision_horizontale = 64
		self.camera_width = 1920
		self.camera_height = 1080

	def DetectAndDisplay(self, frame):
		frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		'''frame_gray = cv.equalizeHist(frame_gray)'''
	
		bottles = self.cascade.detectMultiScale(frame_gray, scaleFactor=1.10, minNeighbors=3)
		frame=cv.rectangle(frame,(384,0),(510,128),(0,255,0),3)
		cv.imshow('Capture', frame)
		cv.waitKey(10)
		print(type(bottles))
		for (x,y,w,h) in bottles:
			x = int(x)
			y = int(y)
			w = int(w)
			h = int(h)
			center=(x+(w/2),y+(h/2))
			a = int(center[0])
			b = int(center[1])
			print(center)
			print(type(center))
			frame=cv.ellipse(frame,(a,b),(w//2,h//2),(255,0,255),4)
			cv.imshow('Capture', frame)
			cv.waitKey(10)
			'''estimation = self.Pose(x,y, w, h)
			self.position_marker(estimation)'''

	def Coordonnee_odom(self, data: Odometry):
		self.position = data.pose

	def Callback_depth(self, data: Image):
		m=1

	def Callback_image(self, data: Image):
		bridge = CvBridge()
		cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
		try:
			self.DetectAndDisplay(cv_image)
		except Exception as err:
			print("Black_Bottle.Callback_image: Erreur ", err)
	
	def Pose(self,x,y,w,h):
		distance = 4000
		for row in self.depth_array[y:y+h, x:x+w]:
			for pixel in row:
				if pixel < distance and pixel != 0:
					distance = pixel  
		angle = ((x+w - self.camera_width/2)/(self.camera_width/2))*(self.vision_horizontale/2) * math.pi / 180
		estimation = Pose()
		estimation.position.x = distance / 1000 * math.cos(angle) 
		estimation.position.y = distance / 1000 * math.sin(angle)  
		return estimation

	def Creation_marqueur(self, pose: Pose):
		stamped = PoseStamped()
		stamped.pose = pose
		stamped.header.frame_id = "/map"
		stamped = self.tfListener.transformPose("/map", stamped)
		marqueur = Marker()
		marqueur.type = Marker.CUBE
		marqueur.action = Marker.ADD
		marqueur.pose = stamped.pose
		marqueur.scale.x = 0.5
		x= int(marqueur.scale.x)
		marqueur.scale.y = 0.5
		x= int(marqueur.scale.x)
		marqueur.color.r = 1.0
		marqueur.color.g = 0.0
		marqueur.color.b = 1.0
		marqueur.color.a = 1.0
		stamped = PoseStamped.create(marqueur.scale.x,marqueur.scale.y)
		self.publisher.publish(stamped)
		self.map.publish(stamped)



def depth_to_color_image_raw_cb(data: Image):
	global node
	node.Callback_depth(data)

def color_image_raw_cb(data: Image):
	global node
	node.Callback_image(data)
	
def odom(data: Odometry):
	global node 
	node.Coordonnee_odom(data)



rospy.init_node('Black_Bottle', anonymous=True)
node = Black_Bottle()
rospy.Subscriber("camera/aligned_depth_to_color/image_raw", Image,depth_to_color_image_raw_cb)
rospy.Subscriber("camera/color/image_raw",Image, color_image_raw_cb)
rospy.Subscriber("/odom", Odometry, odom)
rospy.spin()

