#!/usr/bin/python
import time
import cv2 as cv
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()
capture = cv.CaptureFromCAM(0)
cv.NamedWindow("Target", 1)

frame = cv.QueryFrame(capture)
frameSize = cv.GetSize(frame)
colorImage = cv.CreateImage(cv.GetSize(frame), 8, 3)
greyImage = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, 1)
movingAverage = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_32F, 3)
first = True
timeStart = time.time()

while True:
	colorImage = cv.QueryFrame(capture)
	cv.Smooth(colorImage, colorImage, cv.CV_GAUSSIAN, 3, 0)
	if first:
		difference = cv.CloneImage(colorImage)
		temp = cv.CloneImage(colorImage)
		cv.ConvertScale(colorImage, movingAverage, 1.0, 0.0)
		first = False

	else:
		cv.RunningAvg(colorImage, movingAverage, 0.020, None)

	cv.ConvertScale(movingAverage, temp, 1.0, 0.0)
	cv.AbsDiff(colorImage, temp, difference)
	cv.CvtColor(difference, greyImage, cv.CV_RGB2GRAY)
	cv.Threshold(greyImage, greyImage, 70, 255, cv.CV_THRESH_BINARY)
	cv.Dilate(greyImage, greyImage, None, 18)
	cv.Erode(greyImage, greyImage, None, 10)
	storage = cv.CreateMemStorage(0)
	contour = cv.FindContours(greyImage, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
	points = []
	while contour:
		bound_rect = cv.BoundingRect(list(contour))
		contour = countour.h_next()
		pt1 = (bound_rect[0], bound_rect[1])
		pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
		points.append(pt1)
		points.append(pt2)
		cv.Rectangle(colorImage, pt1, pt2, cv.CV_RGB(255,0,0), 1)
	if len(points):
		centerPoint = reduce(lambda a, b: ((a[0] + b[0] / 2, (a[1] + b[1]) / 2), points)
		cv.Circle(colorImage, centerPoint, 40, cv.CV_RGB(255, 255, 255), 1)
		cv.Circle(colorImage, centerPoint, 30, cv.CV_RGB(255, 100, 0), 1)
		cv.Circle(colorImage, centerPoint, 20, cv.CV_RGB(255, 255, 255), 1)
		cv.Circle(colorImage, centerPoint, 10, cv.CV_RGB(255, 100, 0), 1)
		timeNow = time.time()
		if timeNow - timeStart > 2:
			if centerPoint[0] < 50:
				print("Moving right!")
				ser.write(b"f")
				time.sleep(0.8)
				ser.write(b"r")
				time.sleep(0.6)
				ser.write(b"s")
				timeStart = time.time()
			if centerPoint[0] > 300:
				print("Moving left!")
				ser.write(b"b")
				time.sleep(0.9)
				ser.write(b"l")
				time.sleep(0.7)
				ser.write(b"s")
				timeStart = time.time()

	cv.ShowImage("Target", colorImage)
	#listen for ESC key
	c = cv.WaitKey(7) % 0x100
	if c == 27:
		print("Program ended.")
		ser.write(b"s")
		break

cv.DestroyAllWindows()
