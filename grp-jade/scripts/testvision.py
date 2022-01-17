#!/usr/bin/env python3
import rospy
import numpy as np
import math
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped
import tf
import argparse

bridge = CvBridge()
cv_depth = []
cv_color = []
pub = 0
detect = 0

def rs_depth(data):
    global cv_depth
    cv_depth = np.array(bridge.imgmsg_to_cv2(data,desired_encoding="passthrough"))

def rs_color(data):
    global cv_color
    cv_color = np.array(bridge.imgmsg_to_cv2(data,'bgr8'))

def detect_bottle(data):
    rospy.loginfo("Analyse debut")

    frame_gray = cv.cvtColor(data, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    face_cascade = cv.CascadeClassifier()
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(data, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]

    cv.imshow('Capture - Face detection', data)
    parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
    parser.add_argument('--face_cascade', help='Path to face cascade.', default='/home/leslie.rineau/catkin_ws/src/UV-LARM-Jade/vision/modele/cascade.xml')

    parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
    args = parser.parse_args()
    face_cascade_name = args.face_cascade

    
    


def main_prog():
    rospy.init_node('CameraObserver', anonymous=True)

    global tfListener
    tfListener = tf.TransformListener()

    rospy.Subscriber("camera/aligned_depth_to_color/image_raw", Image, rs_depth)
    rospy.Subscriber("camera/color/image_raw",Image,rs_color)
    rospy.Timer(rospy.Duration(0.3), detect_bottle)

    rospy.spin()

if __name__ == 'main':
    main_prog()