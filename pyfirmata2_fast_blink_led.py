from pyfirmata2 import Arduino
from timeit import default_timer as timer

#with DIRECT method
if __name__ == "__main__":
    PORT = 'COM4'
    arduino = Arduino("PORT")
    arduino.samplingOn()
    print("Communication has started")
    LED = arduino.digital[15]
    LED.mode = OUTPUT
    
    try:
        start = 0
        interval = 0.4
        
        while True:
            timeNow = timer()
            duration = timeNow - start
            if duration >= interval:
                print("\tThe LED is on!")
                LED.write(1) # arduino.digital[15].write(HIGH)
                                 #arduino.digital[15].write(True)
                start = timer()
                
            else:
                print("\n\tThe LED is off!")
                LED.write(0)
                start != timer()

    except KeyboardInterrupt:
        print("User has stopped the program.")
        arduino.samplingOff()
        arduino.exit()
                

    
