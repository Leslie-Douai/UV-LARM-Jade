#!/usr/bin/python3
from __future__ import print_function
from os import posix_fadvise
import cv2 as cv
import argparse
import numpy
import math
import rospy, rospkg
import tf
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, PoseStamped
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
from cv_bridge import CvBridge, CvBridgeError



class BottleDetection():
	def __init__(self):
		self.cascade = cv.CascadeClassifier("grp-jade-challenge2/scripts/cascade.xml")
		self.tfListener = tf.TransformListener()
		self.markerPublisher = rospy.Publisher('/bottle',Marker)
		self.markers_list = list()

	def detectAndDisplay(self, frame):
		frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		frame_gray = cv.equalizeHist(frame_gray)
		color_info = (255, 255, 255)

		bottles = self.cascade.detectMultiScale(frame_gray, minNeighbors=30, scaleFactor=3)
		for (x, y, w, h) in bottles:
			crop_frame = frame[y:y+h, x:x+w]
			median = numpy.median(crop_frame)

			if median > 170 and y > frame.shape[0] / 3:
				cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
				estimated_pose = self.Pose(x,y, w, h)
				self.position_marqueur(estimated_pose)
		
		elements = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]

		estimated_pose = self.Pose(x,y, w, h)
		self.position_marqueur(estimated_pose)

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

	def callback(self):
		m=1

	def callback_image(self, data: Image):
		bridge = CvBridge()
		try:
			cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
			self.detectAndDisplay(cv_image)
		except Exception as err:
			pass

	def position_marqueur(self, pose: Pose):
		if len(self.markers_list) == 0:
			pose_marqueur = self.Creation_marqueur(pose)
			self.markerPublisher.publish(pose_marqueur)
			self.markers_list.append(pose_marqueur)


	def Creation_marqueur(self, pose: Pose):
		pose_stamped = PoseStamped ()
		pose_stamped.pose = pose
		pose_stamped.header.frame_id = "map"
		pose_stamped = self.tfListener.transformPose("map", pose_stamped)
		marker = Marker()
		marker.id = len(self.markers_list)
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





node = BottleDetection()
rospy.init_node('Bottle_Detection', anonymous=True)
rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image,self.Callback)
rospy.Subscriber("camera/color/image_raw",Image, self.callback_image)
rospy.Subscriber("/odom", Odometry, self.Coordonnee_odom)
rospy.spin()

