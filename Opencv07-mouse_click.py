import cv2
import numpy as np
print(cv2.__version__)
evt =-1
coord =[]

img = np.zeros((250,250,3), np.uint8)

def click(event,x,y,flags,params):
    global pnt
    global evt
    if event ==cv2.EVENT_LBUTTONDOWN: # veft click will open this
        print('Mouse Event was : ',event)
        print(x," ",y)
        pnt = (x,y)
        coord.append(pnt)
        print(coord)
        evt = event
    
    if event == cv2.EVENT_RBUTTONDOWN: #right click will open this
        print(x,y)
        blue = frame[y,x,0]
        green = frame[ y,x,1]
        red = frame[y,x,2]
        print(blue,green,red)
        colorstring = str(blue)+ "," +str(green)+","+str(red)
        img[:] =[blue,green,red] 
        fnt =cv2.FONT_HERSHEY_PLAIN
        r =255-int(red)
        g =255-int(green)
        b = 255-int(blue)
        tp =(b,g,r)
        cv2.putText(img,colorstring,(10,25),fnt,1,tp,2)
        cv2.imshow('mycolor',img)


cv2.namedWindow('nanocam')#camera window name
cv2.setMouseCallback('nanocam',click)
cam = cv2.VideoCapture('/dev/video0')
while True:
    ret, frame = cam.read()
    for pnts in coord:
        cv2.circle(frame,pnts,5,(255,0,0),-1)
        font = cv2.FONT_HERSHEY_PLAIN
        mystr = str(pnts)
        cv2.putText(frame, mystr,pnts,font,1.5,(0,255,0),2)


    cv2.imshow('nanocam',frame)
    cv2.moveWindow('nanocam',0,0)
    keyEvent = cv2.waitKey(1)
    if keyEvent == ord('c'):
        coord =[] #clear the screen

    if keyEvent==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
