from pyfirmata2 import Arduino, SERVO
from time import sleep
from timeit import default_timer as timer

port = 'COM5'
board = Arduino(port)

#give 5 secs for Arduino to synch
sleep(5)

start = 0
inteval = 0.015

start2 = 0
interval2 = 0.030

servoPin = 13
board.digital[servoPin].mode = SERVO

def setAngle(servoAngle):
    global servoPin
    board.digital[servoPin].write(servoAngle)

def stop():
    global board
    print("User has finished the program.")
    board.exit()

try: 
    while True:
        timeNow = timer()
        duration1 = timeNow - start1

        if duration1 >= interval1:
            for c in range(0,180,1):
                setAngle(c)
            start1 = timer()

        duration2 = timeNow - start2
        if duration2 >= interval2:
            for i range(180,0,-1):
                setAngle(i)
            start2 = timer()
        
        again = raw_input("Enter 'y' to continue or Press ctrl+C to quit: ")
        if again in 'Yy':
            pass
    
        else:
            print("Please enter a valid answer.")

except KeyboardInterrupt:
    stop()
    
