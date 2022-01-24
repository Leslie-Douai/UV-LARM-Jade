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

# Permet de retrouver le chemin d'un ros package dans tout l'ordi pouir ensuite appliquer ce chemin pour l'appel de la cascade qui est utilisé pour la vision et la détection
def get_pkg_path():
    rospack = rospkg.RosPack()
    return rospack.get_path('grp-jade')

# On commence donc par créer la classe Bottle qui permet la détéction des bouteilles et la mise en place des marqueurs sur la map et dans le topic bottle

class Black_Bottle():
	def __init__(self):
		self.cascade = cv.CascadeClassifier(get_pkg_path() + "/scripts/cascade.xml")
		self.tfListener = tf.TransformListener()
		self.publisher = rospy.Publisher('/bottle',Pose, queue_size=10)
		self.map = rospy.Publisher('/map',Pose, queue_size=10)
		self.vision_horizontale = 64
		self.largeur = 1920
		self.hauteur = 1080

# cette fonction permet d'utiliser la cascade entrainée sur la video que sort la caméra pour ensuite détécter les bouteilles et trouver leur position
	def DetectAndDisplay(self, frame):
		frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		bottles = self.cascade.detectMultiScale(frame_gray, scaleFactor=1.10, minNeighbors=3)
		cv.imshow('Capture - Canette detection', frame)
		cv.waitKey(10)
		for (x,y,w,h) in bottles:
			x = int(x)
			y = int(y)
			w = int(w/2)
			h = int(h/2)
			center=(x+(w/2),y+(h/2))
			a = int(center[0])
			b = int(center[1])
			frame = cv.ellipse(frame,(a,b),(w,h),360,0,360,255,4)
			cv.imshow('Capture', frame)
			cv.waitKey(10)
# N'arrivant pas a récuperer la profondeur via la caméra je n'utilise pas cette partie du code je vais simplement essayer de marquer la position du robot quand il voit une bouteille
			#estimation = self.Pose(x,y,w,h)
			#self.Creation_marqueur(estimation)
			self.publisher.publish(self.position)


	def Coordonnee_odom(self, data: Odometry):
		self.position = data.pose

# cette fonbction ne marchant pas car je me permet de la laisser en commentaire, il s'agissait de recuperer la profondeur de la camera 3d pour ensuite calculer la profondeur de la boutielle dans le décor 
# pour ensuite placer le marqueur correctement
	'''def Callback_depth(self, data: Image):
		bridge = CvBridge()
		self.depth = np.array(bridge.imgmsg_to_cv2(depth_data, "brg8")
		try:
			
		except Exception as err:
			print("Black_Bottle.Callback_depth: Erreur ", err)'''
#cette fonction permet de convertir l'image de la caméra en opencv image pour que la cascade fonctionne
	def Callback_image(self, data: Image):
		bridge = CvBridge()
		cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
		try:
			self.DetectAndDisplay(cv_image)
		except Exception as err:
			print("Black_Bottle.Callback_image: Erreur ", err)
			
# l'objectif de cette fonction est de trouver la position de la bouteille
	def Pose(self,x,y,w,h):
		for row in self.depth_array[y:y+h, x:x+w]:
			for pixel in row:
				if pixel < 2000 and pixel != 0:
					distance = pixel  
		angle = ((x+w - self.hauteur/2)*(self.vision_horizontale/2) * math.pi / 180)/(self.largeur/2)
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
		marqueur.scale.y = 0.5
		marqueur.color.r = 1.0
		marqueur.color.g = 0.0
		marqueur.color.b = 1.0
		marqueur.color.a = 1.0
		stamped = PoseStamped.create(marqueur.scale.x,marqueur.scale.y)
		#print(type(stamped))
		self.publisher.publish(stamped)
		self.map.publish(stamped)



'''def depth_to_color_image_raw_cb(data: Image):
	global node
	node.Callback_depth(data)
'''
def color_image_raw_cb(data: Image):
	global node
	node.Callback_image(data)
	
def odom(data: Odometry):
	global node 
	node.Coordonnee_odom(data)



rospy.init_node('Black_Bottle', anonymous=True)
node = Black_Bottle()
#rospy.Subscriber("camera/aligned_depth_to_color/image_raw", Image,depth_to_color_image_raw_cb)
rospy.Subscriber("camera/color/image_raw",Image, color_image_raw_cb)
rospy.Subscriber("/odom", Odometry, odom)
rospy.spin()

# Tout ce qui est en rapport avec la profondeur est en commentaire
