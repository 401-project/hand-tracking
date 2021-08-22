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


cap=cv2.VideoCapture(0)
p_time=0
c_time=0
while True:
    success , img = cap.read()
    img_RBG= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results= hands.process(img_RBG)
    
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            for id,lm_position in enumerate(hand_lms.landmark):
                # print(id,lm_position)

                high,width,channel= img.shape
                cx,cy= int(lm_position.x*width), int(lm_position.y*high)
                print(cx,cy)
                

                if id==4:
                    cv2.circle(img,(cx,cy),25,(255,255,255),cv2.FILLED)

            mp_draw.draw_landmarks(img, hand_lms , mp_hands.HAND_CONNECTIONS)


    c_time=time.time()
    fps=1/(c_time - p_time)
    p_time=c_time

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    