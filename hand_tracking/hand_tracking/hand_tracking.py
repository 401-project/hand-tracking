import cv2
import mediapipe as mp 
import time

from mediapipe.python.solutions import hands 

cap=cv2.VideoCapture(0)

mp_hands= mp.solutions.hands
hands=mp_hands.Hands()
# print(help(hands))
mp_draw= mp.solutions.drawing_utils

while True:
    success , img = cap.read()
    img_RBG= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results= hands.process(img_RBG)
    
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_lms , mp_hands.HAND_CONNECTIONS)
    
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    