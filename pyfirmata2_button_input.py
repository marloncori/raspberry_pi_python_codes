from pyfirmata2 import Arduino
from timeit import default_timer as timer

start = 0
interval = 0.01

class InputButton(:

    def __init__(self):
        self.PORT = 'COM3'
        self.uno = Arduino(self.PORT)
        self.button = 0
    
    def setup(self):
        print("Setting up the connection to Arduino UNO board...")
        self.uno.samplingOn() #sampling interval of 19ms

    def begin(self):
        self.button = uno.get_pin('d:6:i')
        self.button.enable_reporting()

    def Input(self):
        if str(button.read()) == 'True':
            print("Button has been pressed.")
        elif str(button.red()) == 'False':
            print("Button not pressed.")
        else:
            print("Button has never been pressed.")
            
    def stop(self):
        print("User has stopped the program.")
        self.uno.samplingOff()
        self.uno.exit()


if __name__ == "__main__":

    try:
        setup()
        begin()
        while True:
            timeNow = timer()
            duration = timeNow - start
            if duration >= inter:
                Input()
                start = timer()
            
    except KeyboardInterrupt:
        stop()
