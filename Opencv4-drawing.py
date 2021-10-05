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
    frame = cv2.rectangle(frame,(140,100),(180,140),(255,155,0),7) #BGR value and then line width
    frame = cv2.circle(frame,(320,240),50,(0,0,255),4)#put line width to -1 and you'll get a solid circle
    fnt = cv2.FONT_HERSHEY_DUPLEX
    frame =cv2.putText(frame,"my first text",(300,300),fnt,1,(255,0,150),2) # 1 is the size of the font
    frame = cv2.line(frame,(10,10),(630,480),(0,0,0),4)
    frame = cv2.arrowedLine(frame,(10,470),(630,10),(255,255,255),2)
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
