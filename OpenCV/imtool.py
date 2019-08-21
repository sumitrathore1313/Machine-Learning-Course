import cv2
import numpy as np
import argparse
drawing = False
ix,iy = -1,-1


def mouse_event(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        print ("color rgb", img[iy,ix][0],img[iy,ix][1],img[iy,ix][2])
        print ("position", x, y)
       # print ix,iy
        drawing = False

img = cv2.imread('images/messi.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_event)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()