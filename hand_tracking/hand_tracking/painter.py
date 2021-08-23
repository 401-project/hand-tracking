# from hand_tracking.hand_tracking.hand_tracking import HandDetection
from hand_tracking import *
import cv2 
import numpy as np
import time 
import os 



folder='hand_tracking/Header'
list= os.listdir(folder)
img_list=[]
for path in list:
    image= cv2.imread(f"{folder}/{path}")
    img_list.append(image)

header= img_list[0]
# print(list)

cap= cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4 ,720)

hand_detect = HandDetection(detect_confidance=0.80)

while True:
    success , img =cap.read()
    img= cv2.flip(img,1)
    img= hand_detect.find_hand(img)
    lm_postion= hand_detect.position(img,draw=False)
    
    # if len(lm_postion)!=0:
    #     print(lm_postion)
    
    
    x1,y1=lm_postion[8][1:]
    x2,y2=lm_postion[12][1:]
    
    img[0:125 , 0:1280] = header
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break
