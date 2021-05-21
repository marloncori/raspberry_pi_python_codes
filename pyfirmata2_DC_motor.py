from pyfirmata2 import Arduino
from timeit import default_timer as timer

start1 = 0
interval1 = 0.05
start2 = 0
interval2 = 0.10

class DC_Motor

    def __init__(self): 
        self.PORT = 'COM9'
        self.uno = Arduino(self.PORT)
        self.motorA = 0
        self.motorB = 0
        self.motorEnable = 0
        self.__samplingRate = 100 # 100 Hz
        self.dutyCycle = 0.4 # 40 percent of 100 percent, it is nearly 110-120
        self.increasePWM = True
        
    def begin(self)
        self.motorA = uno.get_pin('d:10:o')
        self.motorB = uno.get_pin('d:11:o')
        self.motorEnable = uno.get_pin('d:12:p')
        self.uno.samplingOn(1000 / self.__samplingRate)

    def __speedControl(self):
        if self.increasePWM:
            seff.dutyCycle += 0.05
            if self.dutyCycle >= 1:
                self.icreasePWM = False
        else:
            self.dutyCycle -= 0.05
            if self.dutyCycle <= 0:
                self.increasePWM = True
        self.motorEnable.write(self.dutyCycle)

    def forward(self):
        print("The DC motor is moving forward!")
        self.motorA.write(True)
        self.motorB.write(False)
        self.__speedControl()
        
    def backward(self):
        print("\nNow the DC motor is moving backward!")
        self.motorA.write(False)
        self.motorB.write(True)
        self._speedControl()
        
    def stop(self):
        print("\nUser has stopped the program.")
        self.motorA.write(False)
        self.motorB.write(False)
        self.uno.samplingOff()
        self.uno.exit()


if __name__ == "__main__":

    try:
        dagu_motor = DC_Motor()
        dagu_motor.begin()
        while True:
            timeNow = timer()

            duration1 = timeNow - start1
            if duration1 >= interval1
                dagu_motor.forward()
                start1 = timer()

            duration2 = timeNow - start2
            if duration2 >= interval2
                dagu_motor.backward()
                start2 = timer()

    except KeyboardInterrupt:
        dagu_motor.stop()
