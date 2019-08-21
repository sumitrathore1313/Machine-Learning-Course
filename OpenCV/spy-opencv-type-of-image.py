# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 02:33:46 2019

@author: sumit
"""

# types of images

import cv2

# read image as rgb
img_color = cv2.imread('images/messi.jpg')

# show image
cv2.imshow('color', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

# read image as gray
img_gray = cv2.imread('images/messi.jpg', 0)

# show image
cv2.imshow('gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# read image as gray
img_gray = cv2.imread('images/messi.jpg', 0)

# convert gray image to binary
thres = 127
ret,thresh_img = cv2.threshold(img_gray,thres,255,cv2.THRESH_BINARY)
thresh_img = thresh_img/255

# show image
cv2.imshow('gray', thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('images/b-messi.jpg', thresh_img)