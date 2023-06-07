import cv2
import os 
import numpy as np
import glob

chessboardSize = (13,9)
frameSize = (1280,720)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm =  17
objp = objp * size_of_chessboard_squares_mm

objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

if os.path.isdir("Image"):
    pass
else:
    os.mkdir("Image")

os.chdir("Image")
i = 0
j = 0
cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
while True:
    ret, frame = cam.read()
    if ret:
        j+=1
        print("Frame recieved: ",j)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret_calib, corners = cv2.findChessboardCorners(gray, chessboardSize, None)
    if ret_calib :
        i+=1
        cv2.imwrite('frame_'+str(i)+'.png',frame)
        print("saved frame no: ",i)
    cv2.imshow('picam',frame)
    cv2.moveWindow('picam',0,0)
    print(frame.shape)
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

print("Frame acceptanca ratio : ",i/j,"\n")

