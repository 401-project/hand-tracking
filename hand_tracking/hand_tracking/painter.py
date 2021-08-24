
from typing import overload
from hand_tracking import *
import cv2 
import numpy as np







folder='hand_tracking/Header'

img_list=[]
image= cv2.imread(f"{folder}/{'1.png'}")
img_list.append(image)
image= cv2.imread(f"{folder}/{'2.png'}")
img_list.append(image)
image= cv2.imread(f"{folder}/{'3.png'}")
img_list.append(image)
image= cv2.imread(f"{folder}/{'4.png'}")
img_list.append(image)



class Draw:
    def __init__(self,img_list) -> None:       
        self.header= img_list[0]
        self.color=(255,0,255)
        self.cap= cv2.VideoCapture(0)
        self.cap.set(3,1280)
        self.cap.set(4 ,720)
        self.hand_detect = HandDetection(detect_confidance=0.80)
        self.brush_weight=15
        self.erase_weight=80
        self.x_previous,self.y_previous=0,0  
        self.img_cover=np.zeros((720, 1280, 3),np.uint8)





    def main(self):
   
        while True:
            success , img =self.cap.read()
            img= cv2.flip(img,1)
            img= self.hand_detect.find_hand(img)
            lm_postion= self.hand_detect.position(img,draw=False)
            
            if len(lm_postion)!=0:
                self.x1,self.y1=lm_postion[8][1:]
                self.x2,self.y2=lm_postion[12][1:]


                fingres=self.hand_detect.find_finger_up()
                # print(fingres)

                if fingres[1] and fingres[2]:
                    x_previous,y_previous=0,0
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
                    if x_previous== 0 and y_previous==0:
                        x_previous,y_previous=x1,y1

                    if color==(0,0,0):
                     cv2.line(img, (x_previous,y_previous),(x1,y1),color,erase_weight)
                     cv2.line(img_cover, (x_previous,y_previous),(x1,y1),color,erase_weight)
                    else:
                     cv2.line(img, (x_previous,y_previous),(x1,y1),color,brush_weight)
                     cv2.line(img_cover, (x_previous,y_previous),(x1,y1),color,brush_weight)
                    x_previous,y_previous=x1,y1


            gray_img=cv2.cvtColor(img_cover,cv2.COLOR_BGR2GRAY)
            _, inverse_img=cv2.threshold(gray_img,0,255,cv2.THRESH_BINARY_INV)
            inverse_img=cv2.cvtColor(inverse_img,cv2.COLOR_GRAY2BGR)
            img=cv2.bitwise_and(img,inverse_img)
            img=cv2.bitwise_or(img,img_cover)


    
            img[0:125 , 0:1280] = header
            cv2.imshow("Image",img)
            if cv2.waitKey(1) & 0xff==ord("q"):
                break
