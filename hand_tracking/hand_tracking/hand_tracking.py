import cv2
import mediapipe as mp 
import time

# from mediapipe.python.solutions import hands 




class HandDetection:
    def __init__(self,detection_mode=False,num_hand=2,detect_confidance=0.5,track_confedince=0.5):
        self.detection_mode=detection_mode
        self.num_hand=num_hand
        self.detect_confidance=detect_confidance
        self.track_confedince=track_confedince
        self.mp_hands= mp.solutions.hands
        self.hands=self.mp_hands.Hands(self.detection_mode,self.num_hand,self.detect_confidance,self.track_confedince)
        self.mp_draw= mp.solutions.drawing_utils
        self.check_hand=False
        self.check_position=False
        self.tip_id=[4,8,12,16,20]
 


    def find_hand(self,img,draw=True):

            img_RBG= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            self.results= self.hands.process(img_RBG)

            
            if self.results.multi_hand_landmarks:
                self.check_hand=True
                for hand_lms in self.results.multi_hand_landmarks:
                    if draw:
                        self.mp_draw.draw_landmarks(img, hand_lms , self.mp_hands.HAND_CONNECTIONS)
            
            return img
            
    def position(self,img,hand_num=0,draw=True):

            self.land_mark_position=[]

            if self.results.multi_hand_landmarks:
                self.check_position=True
                my_hand= self.results.multi_hand_landmarks[hand_num]


                for id,lm_position in enumerate(my_hand.landmark):
                        # print(id,lm_position)

                    high,width,channel= img.shape
                    cx,cy= int(lm_position.x*width), int(lm_position.y*high)
                    # print(cx,cy)
                    self.land_mark_position.append([id,cx,cy])
                    

                    if draw:
                        cv2.circle(img,(cx,cy),25,(255,255,255),cv2.FILLED)
            return self.land_mark_position

    def find_finger_up(self):
        fingers=[]

        if self.land_mark_position[self.tip_id[0]][1] < self.land_mark_position[self.tip_id[0] - 1 ][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        

        for id in range(1,5):
            if self.land_mark_position[self.tip_id[id]][2] < self.land_mark_position[self.tip_id[id]-2][2]:
                fingers.append(1)
            else: 
                fingers.append(0)
        return fingers


                

def main():
    cap=cv2.VideoCapture(0)
    p_time=0
    c_time=0
    checkhand=HandDetection()
    while True:
        success , img = cap.read()
        img =checkhand.find_hand(img)

        c_time=time.time()
        fps=1/(c_time - p_time)
        p_time=c_time

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        
        
        cv2.imshow("Image",img)
        cv2.waitKey(1)
    
if __name__=="__main__":
    main()
    #test













    