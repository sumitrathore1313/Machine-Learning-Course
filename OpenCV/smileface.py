# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 05:28:31 2019

@author: sumit
"""

import numpy as np
import cv2 # OpenCV-Python

# create blank image
img = np.zeros((512, 512, 3), dtype=np.uint8)

# draw a rectangle to cover smile face
cv2.rectangle(img, (50, 50), (450, 450), (255, 255, 255), 3)


# draw a circle face on blank image
cv2.circle(img, (250,250), 150, (0 ,255, 0), 10)

# draw two eyes of smile
cv2.circle(img, (170,200), 20, (0 ,255, 0), -1)
cv2.circle(img, (320,200), 20, (0 ,255, 0), -1)

# draw a line a nose
cv2.line(img, (250, 220), (250, 300), (0, 255, 0), 10)

# draw a happy smile
cv2.ellipse(img, (250, 300), (50,50), 0, 0, 180, (0,250,0), 20)

# write some text
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'Smile', (200,490), font, 1, (255,255,255), 3, cv2.LINE_AA)

# show  image
cv2.imshow('circle image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('images/smile.jpg', img)