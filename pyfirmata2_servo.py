from pyfirmata2 import Arduino, SERVO
from time import sleep

PORT = 'COM4')
uno = Arduino(PORT)
uno.samplingOn()

servo1 = uno.get_pin("d:12:o")
uno.digital[12].mode = SERVO

servo2 = uno.get_pin("d:10:o")
uno.digital[10].mode = SERVO

try:
    while True:
        angle1 = int(input("Enter an angle lower than 180 for the 1st servo: "))
        angle2 = int(input("Now enter angle lower then 180 for the 2nd servo: "))

        for f in range(0,angle1,10):
            servo1.write(f)
        for b in range(angle1,0,20):
            servo1.write(b)

        for c in range(0,angle2,10):                
            servo2.write(c)
        for a in range(angle2,0,20):
            servo2.write(a)

except KeyboardInterrupt:
        print("User has stopped the program.")
        uno.samplingOff()
        uno.exit()
