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
        # self.cap.set(3,1280)
        # self.cap.set(4 ,720)
        self.hand_detect = HandDetection(detect_confidance=0.5)
        self.brush_weight=15
        self.erase_weight=80
        self.x_previous,self.y_previous=0,0  
        self.img_cover=np.zeros((720, 1280, 3),np.uint8)





    def main(self):
   
        while True:
            success , img =self.cap.read()
            img= cv2.flip(img,1)
            img=cv2.resize(img,[1280,720])
            img= self.hand_detect.find_hand(img)
            lm_postion= self.hand_detect.position(img,draw=False)
            
            if len(lm_postion)!=0:
                self.x1,self.y1=lm_postion[8][1:]
                self.x2,self.y2=lm_postion[12][1:]


                fingres=self.hand_detect.find_finger_up()
                # print(fingres)

                if fingres[1] and fingres[2]:
                   self.select_mode(img)
                if fingres[1] and fingres[2]==False:
                    self.draw_mode(img)     


            self.gray_img=cv2.cvtColor(self.img_cover,cv2.COLOR_BGR2GRAY)
            _, self.inverse_img=cv2.threshold(self.gray_img,0,255,cv2.THRESH_BINARY_INV)
            self.inverse_img=cv2.cvtColor(self.inverse_img,cv2.COLOR_GRAY2BGR)
            img=cv2.bitwise_and(img,self.inverse_img)
            img=cv2.bitwise_or(img,self.img_cover)

            img[0:125 , 0:1280] = self.header
            cv2.imshow("Image",img)
            if cv2.waitKey(1) & 0xff==ord("q"):
                break
        
              
    def select_mode(self,img):
        self.x_previous,self.y_previous=0,0
        print("select mode")
        
        if self.y1<125:
            if 250<self.x1<450:
                self.header=img_list[0]
                self.color=(255,0,255)
            elif 550<self.x1<750:
                self.header=img_list[1]
                self.color=(255,0,0)
            elif 800<self.x1<950:
                self.header=img_list[2]
                self.color=(0,255,0)
            elif 1050<self.x1<1200 :
                self.header=img_list[3]
                self.color=(0,0,0)
                
        cv2.rectangle(img,(self.x1,self.y1-21),(self.x2,self.y2+21),self.color, cv2.FILLED)


    def draw_mode(self,img):
        cv2.circle(img,(self.x1,self.y1),15,self.color, cv2.FILLED)

        print("Drawing mode")
        if self.x_previous== 0 and self.y_previous==0:
            self.x_previous,self.y_previous=self.x1,self.y1

        if self.color==(0,0,0):
            print(self.x_previous,"test",self.y_previous)
            cv2.line(img, (self.x_previous,self.y_previous),(self.x1,self.y1),self.color,self.erase_weight)
            cv2.line(self.img_cover, (self.x_previous,self.y_previous),(self.x1,self.y1),self.color,self.erase_weight)        
        else:
            print(self.x_previous,"test",self.y_previous)
            cv2.line(img, (self.x_previous,self.y_previous),(self.x1,self.y1),self.color,self.brush_weight)
            cv2.line(self.img_cover, (self.x_previous,self.y_previous),(self.x1,self.y1),self.color,self.brush_weight)
        self.x_previous,self.y_previous=self.x1,self.y1
    
    
if __name__=="__main__":
    draw=Draw(img_list)
    draw.main()