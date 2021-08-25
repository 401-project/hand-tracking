import cv2
from hand_tracking.hand_tracking.hand_tracking import *

def test_camera_working():
    cap=cv2.VideoCapture(0)
    assert cap

def test_detection_hand():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/hand.jpg")
    test.find_hand(img)
    assert test.check_hand    

def test_target_position():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/hand.jpg")
    test.find_hand(img)
    test.position(img)
    assert test.check_position    
 
