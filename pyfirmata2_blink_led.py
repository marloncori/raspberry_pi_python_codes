import pyfirmata2
from time import sleep

#with INDIRECT method
if __name__ == '__main__':
    arduino = pyfirmata2.Arduino('MY PORT HERE')
    print("Communication has successfully started")
    arduino.samplingOn()
    
    LED = arduino.get_pin("d:11:o")
    start = 0
    interval = 1

    try:
        while True:
            timeNow = timer()
            duration = timeNow - start
            if duration >= interval
                LED.write(1)
                print("LED is bliking!")
                start = timer()
                
            else:
                LED.write(0)
                print("\n")
                start != timer()
                
    except KeyboardInterrupt:
        print("User has stopped the program.")
        arduino.samplingOff()
        arduino.exit()
        
    # led = 11
    # board.digital[led].mode = OUTPUT
    # board.digital[led].write(1)
    # sleep(1)
    #
    # board.digital[led].write(0)
    # sleep(1)
    #              direct method for fast and simple programs
    #