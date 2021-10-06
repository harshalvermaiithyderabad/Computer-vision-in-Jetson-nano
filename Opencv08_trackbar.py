import cv2
print(cv2.__version__)
dispW =620
dispH = 480
def nothing() :
    pass
cam = cv2.VideoCapture('/dev/video0')
cv2.namedWindow('picam')
cv2.createTrackbar('xVal','picam',25,dispW,nothing)# trackbar goes from 0 to 500
cv2.createTrackbar('yVal','picam',25,dispH,nothing)
cv2.createTrackbar('height','picam',0,dispH,nothing)
cv2.createTrackbar('weidth','picam',0,dispW,nothing)

while True:
    ret, frame = cam.read()
    xVal = cv2.getTrackbarPos('xVal','picam')
    yVal = cv2.getTrackbarPos('yVal','picam')
    height = cv2.getTrackbarPos('height','picam')
    weidth =cv2.getTrackbarPos('weidth','picam')
    cv2.rectangle(frame,(xVal,yVal),(xVal+height,yVal + weidth),(255,155,0),7) 
    cv2.circle(frame,(xVal,yVal),5,(255,0,0),-1)
    print(xVal , yVal)


    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
