from threading import Thread
import cv2
import time

class vStream:
    def __init__(self, src):
        """ self is cam1 and src is 1""" 
        self.capture = cv2.VideoCapture(src)
        self.thread = Thread(target= self.update, args= ())
        self.thread.daemon = True
        self.thread.start()
    def update(self):
        while True :
            _,self.frame = self.capture.read()

    def getFrame(self):
        return self.frame
    

cam1 = vStream(0)
cam2 = vStream(2)

while True :
    try:
        myFrame1 = cam1.getFrame()
        myFrame2 = cam2.getFrame()
        myFrame1_resized = cv2.resize(myFrame1, (640, 480)) 
        myFrame2_resized = cv2.resize(myFrame2, (640, 480)) 

        cv2.imshow("webcam1", myFrame1_resized)
        cv2.imshow("webcam2", myFrame2_resized)

    except:
        print("Frame not available \n")

    if cv2.waitKey(1)==ord('q'):
        cam1.capture.release()
        cam2.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        break
