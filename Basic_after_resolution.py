import cv2

cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    ret, frame = cam.read()
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)
    print(frame.shape)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
