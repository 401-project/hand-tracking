import cv2
import mediapipe as mp 
import time

from mediapipe.python.solutions import hands 

cap=cv2.VideoCapture(0)

mp_hands= mp.solutions.hands
hands=mp_hands.Hands()
print(help(hands))


# while True:
#     success , img = cap.read()
    
#     cv2.imshow("Image",img)
#     cv2.waitKey(1)
    