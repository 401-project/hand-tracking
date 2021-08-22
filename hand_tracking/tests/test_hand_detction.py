import cv2

def test_camera_working():
    cap=cv2.VideoCapture(0)
    assert cap