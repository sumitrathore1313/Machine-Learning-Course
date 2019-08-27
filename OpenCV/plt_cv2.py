# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 06:51:11 2019

@author: sumit
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

img_p = plt.imread('images/messi.jpg')
plt.imshow(img_p)

cv2.imshow('rgb image', img_p)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_c = cv2.imread('images/messi.jpg')
plt.imshow(img_c)

cv2.imshow('bgr image', img_c)
cv2.waitKey(0)
cv2.destroyAllWindows()


img_c = cv2.cvtColor(img_c, cv2.COLOR_BGR2RGB)
cv2.imshow('bgr image', img_c)
cv2.waitKey(0)
cv2.destroyAllWindows()