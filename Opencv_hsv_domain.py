import cv2
print(cv2.__version__)
dispW =320
dispH =240
flip =2
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=1920, height=1080, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camset) for raspberry pi camera
cam = cv2.VideoCapture('/dev/video0')
fourcc =cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/myCam3.avi',fourcc,21,(640,480))
while True:
    ret, frame = cam.read()
    cv2.imshow('picam',frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    out.write(hsv)
    cv2.imshow("original",frame)
    cv2.imshow('frame',hsv)
    cv2.moveWindow('picam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()
