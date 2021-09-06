#!/usr/bin/env python
# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	vs = VideoStream(src=0).start()

# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])

# allow the camera or video file to warm up
time.sleep(2.0)

Click here to download the source code to this post
ball-tracking-animated-02

Today marks the 100th blog post on PyImageSearch.

100 posts. It’s hard to believe it, but it’s true.

When I started PyImageSearch back in January of 2014, I had no idea what the blog would turn into. I didn’t know how it would evolve and mature. And I most certainly did not know how popular it would become. After 100 blog posts, I think the answer is obvious now, although I struggled to put it into words (ironic, since I’m a writer) until I saw this tweet from @si2w:

Big thanks for @PyImageSearch, his blog is by far the best source for projects related to OpenCV.

I couldn’t agree more. And I hope the rest of the PyImageSearch readers do as well.

It’s been an incredible ride and I really have you, the PyImageSearch readers to thank. Without you, this blog really wouldn’t have been possible.

That said, to make the 100th blog post special, I thought I would do something a fun — ball tracking with OpenCV:

The goal here is fair self-explanatory:

Step #1: Detect the presence of a colored ball using computer vision techniques.
Step #2: Track the ball as it moves around in the video frames, drawing its previous positions as it moves.
The end product should look similar to the GIF and video above.

After reading this blog post, you’ll have a good idea on how to track balls (and other objects) in video streams using Python and OpenCV.


Looking for the source code to this post?
JUMP RIGHT TO THE DOWNLOADS SECTION 
Ball tracking with OpenCV
Let’s get this example started. Open up a new file, name it ball_tracking.py , and we’ll get coding:

# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

#lines 2-8 handle importing our necessary packages. We’ll be using deque , a list-like data structure with super fast appends and pops to maintain a list of the past N (x, y)-locations of the ball in our video stream. Maintaining such a queue allows us to draw the “contrail” of the ball as its being tracked.
#We’ll also be using imutils , my collection of OpenCV convenience functions to make a few basic tasks (like resizing) much easier. If you don’t already have imutils installed on your system, you can grab the source from GitHub or just use pip to install it:
#$ pip install --upgrade imutils
#From there, Lines 11-16 handle parsing our command line arguments. The first switch, --video is the (optional) path to our example video file. If this switch is supplied, then OpenCV will grab a pointer to the video file and read frames from it. Otherwise, if this switch is not supplied, then OpenCV will try to access our webcam.
#If this your first time running this script, I suggest using the --video switch to start: this will demonstrate the functionality of the Python script to you, then you can modify the script, video file, and webcam access to your liking.
#A second optional argument, --buffer is the maximum size of our deque , which maintains a list of the previous (x, y)-coordinates of the ball we are tracking. This deque allows us to draw the “contrail” of the ball, detailing its past locations. A smaller queue will lead to a shorter tail whereas a larger queue will create a longer tail (since more points are being tracked):
#Figure 1: An example of a short contrail (buffer=32) on the left, and a longer contrail (buffer=128) on the right. Notice that as the size of the buffer increases, so does the length of the contrail.
#Figure 1: An example of a short contrail (buffer=32) on the left, and a longer contrail (buffer=128) on the right. Notice that as the size of the buffer increases, so does the length of the contrail.
#Now that our command line arguments are parsed, let’s look at some more code:

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	vs = VideoStream(src=0).start()

# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])

# allow the camera or video file to warm up
time.sleep(2.0)
#Lines 21 and 22 define the lower and upper boundaries of the color green in the HSV color space (which I determined using the range-detector script in the imutils library). These color boundaries will allow us to detect the green ball in our video file. Line 23 then initializes our deque of pts using the supplied maximum buffer size (which defaults to 64 ).
#From there, we need to grab access to our vs pointer. If a --video switch was not supplied, then we grab reference to our webcam (Lines 27 and 28) — we use the imutils.video VideoStream threaded class for efficiency. Otherwise, if a video file path was supplied, then we open it for reading and grab a reference pointer on Lines 31 and 32 (using the built in cv2.VideoCapture ).

# keep looping
while True:
	# grab the current frame
	frame = vs.read()

	# handle the frame from VideoCapture or VideoStream
	frame = frame[1] if args.get("video", False) else frame

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break

	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)

	# update the points queue
	pts.appendleft(center)

	# loop over the set of tracked points
	for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue

		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
            break

# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
	vs.stop()

# otherwise, release the camera
else:
	vs.release()

# close all windows
cv2.destroyAllWindows()
