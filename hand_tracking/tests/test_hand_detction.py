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
 
def test_no_detection_hand():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/logo.jpeg")
    test.find_hand(img)
    assert test.check_hand  == False  

def test_no_target_position():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/logo.jpeg")
    test.find_hand(img)
    test.position(img)
    assert test.check_position  == False   
    
def test_fingers_up():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/hand2.jpg")
    test.find_hand(img)
    test.position(img)
    actual =test.find_finger_up()
    expected = [1, 1, 1, 1, 1]
    assert actual == expected   
    

def test_one_finger_up():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/one_finger_up.png")
    test.find_hand(img)
    test.position(img)
    actual =test.find_finger_up()
    expected = [0, 1, 0, 0, 0]
    assert actual == expected  
    

def test_two_fingers_up():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/two_fingers.png")
    test.find_hand(img)
    test.position(img)
    actual =test.find_finger_up()
    expected = [0, 1, 1, 0, 0]
    assert actual == expected   



def test_no_fingers_up():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/close_hand.png")
    test.find_hand(img)
    test.position(img)
    actual =test.find_finger_up()
    expected = [0, 0, 0, 0, 0]
    assert actual == expected  
    
def test_select_mode():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/two_fingers.png")
    test.find_hand(img)
    test.position(img)
    test.find_finger_up()
    assert test.select 


def test_not_select_mode():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/one_finger_up.png")
    test.find_hand(img)
    test.position(img)
    test.find_finger_up()
    assert test.select == False
   
def test_draw_mode():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/one_finger_up.png")
    test.find_hand(img)
    test.position(img)
    test.find_finger_up()
    assert test.draw 
    
     
def test_not_draw_mode():
    test=HandDetection()
    img = cv2.imread("hand_tracking/hand_tracking/assest/two_fingers.png")
    test.find_hand(img)
    test.position(img)
    test.find_finger_up()
    assert test.draw == False