#!/usr/bin/env python
import numpy as np
import cv2 as cv

green = np.uint8([[[0,255,0 ]]])
hsv_green = cv.cvtColor(green,cv2.COLOR_BGR2HSV)
print hsv_green
