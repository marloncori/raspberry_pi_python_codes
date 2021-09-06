#
#Jiaxuan Su (js3596), Jonathan Nusantara (jan265)
#
Ball tracking program
#

import pygame
from pygame.locals import *
import os
import RPi.GPIO as GPIO
import time
import subprocess
import cv2
import numpy as np
import math

#Run fix touchscreen script
subprocess.check_output("./fix_touchscreen", shell = True)

# Environment setup for PiTFT
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb0')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

# Pygame initialization
pygame.init()
pygame.mouse.set_visible(True)
size = width, height = 320, 240
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0, 255, 0
screen = pygame.display.set_mode(size)
my_font = pygame.font.Font(None, 20)
start_button = {'Start': (160, 90)}
stop_button = {'Stop': (160, 90), 'Distance from ball': (110, 150)}

start_time_prog = time.time()

# Set GPIO channels
GPIO.setmode(GPIO.BCM)
# Motor A
GPIO.setup(26, GPIO.OUT) #PWMA
GPIO.setup(5, GPIO.OUT) #AI1
GPIO.setup(6, GPIO.OUT) #AI2
# Motor B
GPIO.setup(20, GPIO.OUT) #PWMB
GPIO.setup(12, GPIO.OUT) #BI1
GPIO.setup(16, GPIO.OUT) #BI2

# Motor initialization
left = GPIO.PWM(26, 50)
left.start(50)
right = GPIO.PWM(20, 50)
right.start(50)
GPIO.output(5, 0) # Set AI1 to low
GPIO.output(6, 0) # Set AI2 to low
GPIO.output(12, 0) # Set BI1 to low
GPIO.output(16, 0) # Set BI2 to low

# Robot mode variables
# 0 = stop, 1 = ball tracking, 2 = manual forward, 3 = manual backward
# 0 can be called anytime. 1, 2, and 3 can only be called from 0
global robot_mode
robot_mode = 0
global prev_robot_mode
prev_robot_mode = 0
global run #Program run flag
run = 1
global start #If start program
start = 0
ball_detected = 0 #If track the ball

# Constants
KERNEL_MORPH_BALL = np.ones((3,3),np.uint8)
KERNEL_MORPH_HAND = np.ones((4,4),np.uint8)
FOCAL = 220 # camera focal length
WIDTH_BALL = 3.35 # width of tennis ball

# HSV threshold of ball and hand
# Need to be adjusted depending on camera exposure and environment
# Glove HSV range 
lower_hand = (91,155,0)
upper_hand = (123,255,65)
# Detect based on tennis ball color
lower_ball = (22, 30, 0)
upper_ball = (40, 255, 113)

# variables and list for functionalities
ball_x = [] # x axis coordinate of ball center
ball_rad = [] # Radius of ball center
dist_x = 0 # Pixel coordinate of ball center
dist_rad = 0 # Pixel radius of circle
defects_list = []
ball_last_detected = time.time()
ball_first_detected = 0
ball_verify = 0
motor_time = 0
mask_ball = 0

# Variables for modes and motor control
finger = 0 # Number for stop state
dist_calc = 0 # Distance of ball from camera in cm
dist_l = 0 # Pixel distance of circle from left of camera view
dist_r = 0 # Pixel distance of circle from right of camera view
dist_l_pre = 0 # Previous pixel distance of circle from left of camera view
dist_r_pre = 0 # Previous pixel distance of circle from right of camera view
left_speed = 0
right_speed = 0

# Take input from webcam
cap = cv2.VideoCapture(-1) # 640x480

# Reduce the size of video to 320x240 so rpi can process faster
cap.set(3,320)
cap.set(4,240)


# Distance average function for ball tracking
def average_distance(distance_list, length): 
    total = 0
    for i in distance_list:
        total += i
    return total / length
    
def average_defects(defects_list):
	return
    
# Ball tracking function
def ball_track():
    global mask_ball, ball_x, ball_rad, dist_x, dist_l, dist_r, dist_rad, dist_calc, ball_detected, ball_last_detected, ball_first_detected, ball_verify
    
    blurred = cv2.GaussianBlur(frame, (7, 7), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask_ball = cv2.inRange(hsv, lower_ball, upper_ball)
    mask_ball = cv2.erode(mask_ball, KERNEL_MORPH_BALL, iterations=2)
    mask_ball = cv2.dilate(mask_ball, KERNEL_MORPH_BALL, iterations=5)
    mask_ball = cv2.GaussianBlur(mask_ball,(11,11),0)

    # Detect circles using HoughCircles
    # param is threshold of size of circle
    # If param2 is low, more sensitive to small circles and false positive
    circles = cv2.HoughCircles(mask_ball,cv2.HOUGH_GRADIENT,2,120,param1=100,param2=45,minRadius=2,maxRadius=0)     

    #Draw Circles
    if circles is not None:
        # If ball was previously not detected
        if ball_detected == 0 and ball_verify == 0:
            ball_first_detected = time.time()
            ball_verify = 1
        if ball_verify == 1 and (time.time() - ball_first_detected) > 0.1: # Verification after .1 second passes, ball still detected
            ball_detected = 1
            ball_verify = 0
        if ball_detected == 1:    
            ball_last_detected = time.time() # Update last detected time of the ball
            for i in circles[0,:]:
                cv2.circle(frame,(int(round(i[0])),int(round(i[1]))),int(round(i[2])),(0,255,0),5) # x is 320 y is 240, draw circle  
                ball_x.append(round(i[0])) # Append x center coordinate to list
                ball_rad.append(round(i[2])) # Append radius to list
                
                # Average every 4 entries
                if len(ball_x) == 4: 
                    dist_x = average_distance(ball_x, 4) # x coordinate of ball center
                    ball_x = []
                    
                    # Calculated distance of ball from camera
                    dist_rad = average_distance(ball_rad, 4) 
                    dist_calc = WIDTH_BALL * FOCAL / dist_rad
                    ball_rad = []
                    
                    # For output to control algorithm
                    dist_r = round(320 - (dist_x + dist_rad), 2)
                    dist_l = round(dist_x - dist_rad, 2)
                
                    # Focal distance calculation
                    # focal = (dist_ave * 25.4 / 3.35) # in pixels and cm
    else:
        if ball_verify == 1: # During ball dection verification process, if ball is lost means false positive
            ball_verify = 0
        
        ball_lost_time = time.time() - ball_last_detected
        dist_calc = 0 # Reset ball distance
        
        # maybe use ball lost time for rotate, but immediately set ball_detected = 0
        if ball_detected == 1 and ball_lost_time > 2: # If ball has been missing for > 2 seconds
            ball_detected = 0 # Ball is not detected / not in frame -> need to find ball
            
            
                    
# Finger detection function
def hand_gesture():
    global mask_hand, finger, defects_list
    try:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)        

        # Get only glove color
        mask_hand = cv2.inRange(hsv, lower_hand, upper_hand)
        
        # Noise filtering
        mask_hand = cv2.GaussianBlur(mask_hand,(5,5),0)
        
        # Erosion and dilation (need to be adjusted)
        mask_hand = cv2.erode(mask_hand,KERNEL_MORPH_HAND,iterations = 1)
        mask_hand = cv2.dilate(mask_hand,KERNEL_MORPH_HAND,iterations = 2)
        
        # Noise filtering
        mask_hand = cv2.GaussianBlur(mask_hand,(5,5),0) 
     
        # Find contour
        contours,hierarchy= cv2.findContours(mask_hand,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        # Get max area in detected contour (which is the hand)
        area_max = 0
        contour_index = 0
        for i in range(len(contours)):
            cnt = contours[i]
            area_temp = cv2.contourArea(cnt)
            if area_temp > area_max:
                area_max = area_temp
                contour_index = i
        cnt = contours[contour_index]
        
        # Create convex hull of hand
        hull = cv2.convexHull(cnt)
                
        # Smooth and approximate the contour
        cnt_ap= cv2.approxPolyDP(cnt,0.0005*cv2.arcLength(cnt,True),True)

        # Calculate contour and hull area
        # To compare finger digit 0 or 1
        area_cnt = cv2.contourArea(cnt)
        area_hull = cv2.contourArea(hull)
        
        # Recalculate hull and calculate defects
        # Need returnPoints to be False
        hull = cv2.convexHull(cnt_ap, returnPoints=False)
        defects = cv2.convexityDefects(cnt_ap, hull)
        
        defects_count=0
        # Loop to find number of defects
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt_ap[s][0])
            end = tuple(cnt_ap[e][0])
            far = tuple(cnt_ap[f][0])
            
            # Triangle lengths
            a = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            b = math.sqrt((far[0] - end[0])**2 + (far[1] - end[1])**2)
            c = math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2)

            # Calculate angle using cosine rule
            angle = math.acos((a**2 + b**2 - c**2) / (2 * a * b)) * 57.295
            
            # If angle <90, it is a defect caused by finger raised
            if angle < 90:
                defects_count += 1
        
        # Append defects count to list
        defects_list.append(defects_count)
        
        if len(defects_list) == 10:
            defects_most = max(defects_list,key=defects_list.count)
            defects_list = []
            # Finger print
            # 0 defect = finger 0 or 1
            if area_cnt > 4000: # If there is hand
                if defects_most == 0:
                    # If hull is 10% bigger than contour => finger 1
                    if (area_hull-area_cnt)/(area_cnt) > .15: 
                        finger = 1
                    else:
                        finger = 0
                 
                # 1 defect => finger 2
                elif defects_most == 1:
                    finger = 2
            
                # 2 defects => finger 3
                elif defects_most == 2 :
                    finger = 3
            
            # Detect only 0 - 3 fingers

    except Exception:
        pass


# Motor movement function
def rotate():
    left.ChangeDutyCycle(27)
    right.ChangeDutyCycle(27)
    GPIO.output(5, 1)
    GPIO.output(6, 0)
    GPIO.output(12, 0)
    GPIO.output(16, 1)
    
def forward():
    if robot_mode == 2:
        left.ChangeDutyCycle(40)
        right.ChangeDutyCycle(40)
    GPIO.output(5, 1)
    GPIO.output(6, 0)
    GPIO.output(12, 1)
    GPIO.output(16, 0)

def backward():
    left.ChangeDutyCycle(40)
    right.ChangeDutyCycle(40)
    GPIO.output(5, 0)
    GPIO.output(6, 1)
    GPIO.output(12, 0)
    GPIO.output(16, 1)
    
def stop():


    GPIO.output(5, 0)
    GPIO.output(6, 0)
    GPIO.output(12, 0)
    GPIO.output(16, 0)

# Set motor speed function
def set_speed():
    global dist_l_pre, dist_r_pre, left_speed, right_speed, motor_time
    
    k_p = 0.05
    k_i = 0
    k_d = 0
    #d_time = time.time() - motor_time
    if dist_calc > 15:
        if dist_calc > 25:
            k = 35
        else:
            k = 25    
        GPIO.output(5, 1)
        GPIO.output(6, 0)
        GPIO.output(12, 1)
        GPIO.output(16, 0)
        
        left_speed = k + k_p * dist_r #+ k_d * ((dist_r - dist_r_pre) / d_time)
        right_speed = k + k_p * dist_l #+ k_d * ((dist_l - dist_l_pre) / d_time)

        left.ChangeDutyCycle(left_speed)
        right.ChangeDutyCycle(right_speed)        

    elif dist_calc > 8: # between 8 and 13, re-center only
        left.ChangeDutyCycle(20)
        right.ChangeDutyCycle(20)
        if dist_l + 40 < dist_r: # If ball is a bit right, do clockwise
            GPIO.output(5, 1)
            GPIO.output(6, 0)
            GPIO.output(12, 0)
            GPIO.output(16, 1)
        elif dist_r + 40 < dist_l: # If ball is a bit right, do counter-clockwise
            GPIO.output(5, 0)
            GPIO.output(6, 1)
            GPIO.output(12, 1)
            GPIO.output(16, 0)
        else: # Stop moving
            GPIO.output(5, 0)
            GPIO.output(6, 0)
            GPIO.output(12, 0)
            GPIO.output(16, 0)
            
            
    else: # When ball is close
        left_speed = 0
        right_speed = 0
        left.ChangeDutyCycle(left_speed)
        right.ChangeDutyCycle(right_speed)

        
#Display start button
screen.fill(black)
pygame.draw.circle(screen, green, (160, 90), 30)
for my_text, text_pos in start_button.items():
    text_surface = my_font.render(my_text, True, white)
    rect = text_surface.get_rect(center=text_pos)
    screen.blit(text_surface, rect)
pygame.display.flip()

#Main loop
while run:
    start_loop = time.time()
    _, frame = cap.read() # Read image frames from live video feed
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GPIO.cleanup()
            sys.exit()
        if (event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif (event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x, y = pos
            if 130 < x < 190 and 60 < y < 120:
                if robot_mode == 0:
                    prev_robot_mode = robot_mode
                    finger = 1
                    robot_mode = 1
                elif robot_mode != 0:
                    prev_robot_mode = robot_mode
                    finger = 0
                    robot_mode = 0
    
    # Checking for different robot modes
    if robot_mode == 0: # Stop
        if prev_robot_mode != 0:
            stop()
        hand_gesture()
        prev_robot_mode = robot_mode
        robot_mode = finger
    
    elif robot_mode == 1: # Ball tracking
        ball_track()
        if ball_detected:
            #stop()
            #forward()
            set_speed()
            dist_l_pre = dist_l
            dist_r_pre = dist_r
        else:
            rotate()
        hand_gesture()
        if finger == 0: # Stop detected
            # Reset variables
            ball_detected = 0
            ball_verify = 0
            # Change mode
            prev_robot_mode = robot_mode
            robot_mode = finger
    
    elif robot_mode == 2: # Forward
        if prev_robot_mode != 2:
            forward()
        prev_robot_mode = robot_mode
        hand_gesture()
        if finger == 0 or finger == 3: # From forward, can only stop or backward
            prev_robot_mode = robot_mode
            robot_mode = finger
    
    elif robot_mode == 3: # Backward
        if prev_robot_mode != 3:
            backward()
        prev_robot_mode = robot_mode    
        hand_gesture()
        if finger == 0 or finger == 2: # From backward, can only stop or forward
            prev_robot_mode = robot_mode
            robot_mode = finger
    
    
    # Video display
    # cv2.imshow('tracking',frame)
    # cv2.imshow('Ball mask',mask_ball)
    # cv2.imshow('hand mask',mask_hand)    
    
    # # Display PiTFT buttons
    if robot_mode != 0:
        pygame.draw.circle(screen, red, (160, 90), 30) # Draw stop button
        for my_text, text_pos in stop_button.items():
            text_surface = my_font.render(my_text, True, white)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        my_text = str(round(dist_calc))    
        text_surface = my_font.render(my_text, True, white)
        rect = text_surface.get_rect(center=(210,150))
        screen.blit(text_surface, rect)

    else:
        pygame.draw.circle(screen, green, (160, 90), 30) # Draw start button
        for my_text, text_pos in start_button.items():
            text_surface = my_font.render(my_text, True, white)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
    
    # Display motor mode
    my_text = "motor mode"
    text_surface = my_font.render(my_text, True, white)
    rect = text_surface.get_rect(center=(100,190))
    screen.blit(text_surface, rect)
    my_text = str(robot_mode)
    text_surface = my_font.render(my_text, True, white)
    rect = text_surface.get_rect(center=(210,190))
    screen.blit(text_surface, rect)        
  
    pygame.display.flip()

    # Program imeout
    if (time.time() - start_time_prog) > 300: 
        run = False
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

stop()
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()
}
