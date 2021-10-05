import cv2
print(cv2.__version__)
dispW =1280
dispH =960
flip =2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam = cv2.VideoCapture(camset) for raspberry pi camera
cam = cv2.VideoCapture('/dev/video0')
#cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    ret, frame = cam.read()
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',700,0)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameSmall =cv2.resize(frame,(320,240))
    graySmall =cv2.resize(gray,(320,240))
    cv2.moveWindow('BW',0,256)
    cv2.moveWindow('nanoSmall',0,0)
    cv2.imshow("BW",graySmall)
    cv2.imshow('nanoSmall',frameSmall)


    cv2.moveWindow('BW2',385,265)
    cv2.moveWindow('nanocam2',385,0)
    cv2.imshow("BW2",graySmall)
    cv2.imshow('nanocam2',frameSmall)


    if cv2.waitKey(1)==ord('q'):
        break

cam.release()                    
cv2.destroyAllWindows()
