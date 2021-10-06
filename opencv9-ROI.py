import cv2
print(cv2.__version__)
dispW =1280
dispH =960
flip =2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camset) for raspberry pi camera
cam = cv2.VideoCapture('/dev/video0')
while True:
    ret, frame = cam.read()
    roi =frame[50:250,200:400].copy() # creating copy so that roi is not white
    roiGray = cv2.cvtColor(roi,cv2.COLOR _BGR2GRAY)
    roiGray = cv2.cvt.Color(roiGray,cv2.COLOR_GRAY2BGR)
    frame[50:250,200:400] = [255,255,255]  #he pixel region is totally white 
    frame[50:250,200:400] = roiGray
    cv2.imshow("Gray_roi",roiGray)
    cv2.moveWindow("Gray_roi",705,250)
    cv2.imshow("ROI",roi)
    cv2.moveWindow('ROI',705,0)
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

# the IDE might not respond always, close the idea and start again