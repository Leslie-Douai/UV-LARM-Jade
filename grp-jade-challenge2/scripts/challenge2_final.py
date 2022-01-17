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



path_cascade = "larm1_slam/scripts/cascade.xml"
bottle_cascade = cv2.CascadeClassifier(path_cascade)
tfListener = tf.TransformListener()
rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image, depthCallback)
rospy.Subscriber("camera/color/image_raw",Image, rgbImageCallback)
rospy.Subscriber("/odom", Odometry, odomCoordinates)
markerPublisher = rospy.Publisher('/bottle',Marker)
markers_list = list()
        

def detectAndDisplay(self, frame):
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)
        color_info = (255, 255, 255)

        black_bottle = bottle_cascade.detectMultiScale(frame_gray, minNeighbors=30, scaleFactor=3)
        for (x, y, w, h) in black_bottle:
            crop_frame = frame[y:y+h, x:x+w]
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            estimated_pose = estimatePose(x,y, w, h)
            handle_markers(estimated_pose)
        
        elements = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
        if len(elements) > 0:
            l = max(elements, key=cv.contourArea)
            x,y,w,h = cv.boundingRect(l)
            if w > 10 and y < 500:
                estimated_pose = estimatePose(x,y, w, h)
                handle_markers(estimated_pose)

    def estimatePose(self, x, y, w, h):
        distance = 2000
        for row in depth_array[y:y+h, x:x+w]:
            for pixel in row:
                if pixel < distance and pixel != 0:
                    distance = pixel  # ros distance with realsense camera
        angle = ((x+w - camera_width/2)/(camera_width/2))*(hfov/2) * math.pi / 180
        estimated_pose = Pose()
        estimated_pose.position.x = distance / 1000 * math.cos(angle) 
        estimated_pose.position.y = distance / 1000 * math.sin(angle) 
        return estimated_pose


    def odomCoordinates(self, data: Odometry):
        position = data.pose

    def depthCallback(self, data):
        bridge = CvBridge()

        # Try to convert the ROS Image message to a CV2 Image
        try:
            cv_image = bridge.imgmsg_to_cv2(data)
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))
        # show_image(cv_image)
        depth_array = numpy.array(cv_image, dtype=numpy.float32)
        #print("min : " + str(numpy.amin(depth_array)) + "; max : " + str(numpy.amax(depth_array)))

    def rgbImageCallback(self, data: Image):
        bridge = CvBridge()
        # Try to convert the ROS Image message to a CV2 Image
        try:
            cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))
        detectAndDisplay(cv_image)


    def handle_markers(self, pose: Pose):
        
        '''if marker is not in area of already existing marker
                then publish marker
            else if position estimated has changed significantly
                then delete marker in area and publish new one
            else 
                do nothing'''
        
        if len(markers_list) == 0:
            marker_to_publish = generateMarker(pose)
            markerPublisher.publish(marker_to_publish)
            markers_list.append(marker_to_publish)
            #print(markers_list)
            #print(len(markers_list))
            #print("Marker Published because first one")

        for existing_marker in markers_list:
            if areNotInSameArea(existing_marker.pose, pose):
                marker_to_publish = generateMarker(pose)
                markerPublisher.publish(marker_to_publish)
                markers_list.append(marker_to_publish)
                #print("Marker Published because not in area")

            elif positionChangedSignificantly(existing_marker.pose, pose):
                # Delete current marker 
                existing_marker.action = Marker.DELETE
                markerPublisher.publish(existing_marker)
                markers_list.remove(existing_marker)
                
                #print("Marker Deleted because position changed")
                newest_marker = generateMarker(pose)
                markerPublisher.publish(newest_marker)
                markers_list.append(newest_marker)
                #print("Marker Published because position changed")

    def areNotInSameArea(self, existing_marker: Pose, new_marker: Pose):
        a = numpy.array((existing_marker.position.x, existing_marker.position.y))
        b = numpy.array((new_marker.position.x, new_marker.position.y))
        dist = numpy.linalg.norm(a-b)
        #print("!!!! DISTANCE : " + str(dist) + " are in same area : " + str(dist<10))
        return dist > 5

    def positionChangedSignificantly(self, existing_marker: Pose, new_marker: Pose):
        diff_x = abs(existing_marker.position.x - new_marker.position.x)
        diff_y = abs(existing_marker.position.y - new_marker.position.y)
        #print("delta x : " + str(diff_x) + "; delta y : " + str(diff_y))
        bool_val = abs(existing_marker.position.x - new_marker.position.x) > 0.2 or abs(existing_marker.position.y - new_marker.position.y) > 0.4
        #print("!!!! CHANGED : " + str(bool_val))
        return bool_val

    def generateMarker(self, pose: Pose):
        pose_stamped = PoseStamped ()
        pose_stamped.pose = pose
        pose_stamped.header.frame_id = "map"
        pose_stamped = tfListener.transformPose(
            "map", pose_stamped)
        marker = Marker()
        marker.header.frame_id = "camera_link"
        marker.id = len(markers_list)
        print("MARKER ID : " + str(marker.id))
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        marker.pose = pose_stamped.pose
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 0.0
        marker.color.b = 1.0
        return marker




rospy.init_node('Blackbottle_Detection', anonymous=True)
node = BlackbottleDetection()
rospy.spin()
    except rospy.ROSInterruptException:
        pass
