import cv2 as cv
import time
import serial

#communicate with Arduino UNO through serial port
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser.flush()

cv.NamedWindow("camera", 1)
cap = cv.CaptureFromCAM(0)
cv.SetCaptureProperty(cap, 3, 360)
cv.SetCaptureProperty(cap, 4, 240)
timeStart = time.time()
time.sleep(1)
while True:
	img = cv.QueryFrame(cap)
	cv.Smooth(img, img, cv.CV_BLUR, 3)
	hue_img = cv.CreateImage(cv.GetSize(img), 8, 3)
	cv.CvtColor(img, hue_img, cv.CV_BGR2HSV)
	threshold_img = cv.CreateImage(cv.GetSize(hue_img), 8, 1)
	cv.InRangeS(hue_img, (10, 120, 60), (20, 255, 255), threshold_img)
	storage = cv.CreateMemStorage(0)
	contour = cv.FindContours(threshold_img, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
	points = []
	while contour:
		rect = cv.BoundingRect(list(contour))
		contour = countour.h_next()
		size = (rect[2] * rect[3])
		if size > 100:
			pt1 = (rect[0], rect[1])
			pt2 = (rect[0] + rect[2], rect[1] + rect[3])
			cv.Rectangle(img, pt1, pt2, (38, 160, 60))
			timeNow = time.time()
			if timeNow - timeStart > 1:
				if rect[0] < 10:
					print("moving right...")
					ser.write(b"f")
					time.sleep(0.7)
					ser.write(b"s")
					timeStart = time.time()

				if rect[0] + rect[2] > 310:
					print("moving left...")
					ser.write(b"b")
					time.sleep(0.7)
					ser.write(b"s")
					timeStart = time.time()

				if rect[2] > 60:
					print("backing up...")
					ser.write(b"l")
					time.sleep(0.8)
					ser.write(b"s")
					timeStart = time.time()

				if rect[2] < 40:
					print("moving forward...")
					ser.write(b"r")
					time.sleep(0.8)
					ser.write(b"s")
					timeStart = time.time()

	cv.ShowImage("Color Tracking", img)
	if cv.WaitKey(10) == 27:
		print("Program ended!")
		ser.write(b"s")
		break

cv.DestroyAllWindows()
