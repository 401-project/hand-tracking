# from hand_tracking.hand_tracking.hand_tracking import HandDetection
from typing import overload
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
color=(255,0,255)
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
    
    if len(lm_postion)!=0:
    #     print(lm_postion)
    
    
        x1,y1=lm_postion[8][1:]
        x2,y2=lm_postion[12][1:]
        print(x1)

        fingres=hand_detect.find_finger_up()
        # print(fingres)

        if fingres[1] and fingres[2]:
            print("select mode")
            if y1<125:
                if 250<x1<450:
                    header=img_list[0]
                    color=(255,0,255)
                elif 550<x1<750:
                    header=img_list[1]
                    color=(255,0,0)
                elif 800<x1<950:
                    header=img_list[2]
                    color=(0,255,0)
                elif 1050<x1<1200 :
                    header=img_list[3]
                    color=(0,0,0)
                    
            cv2.rectangle(img,(x1,y1-21),(x2,y2+21),color, cv2.FILLED)




        if fingres[1] and fingres[2]==False:
            cv2.circle(img,(x1,y1),15,color, cv2.FILLED)

            print("Drawing mode")
    
    # img[0:125 , 0:1280] = header
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xff==ord("q"):
        break
