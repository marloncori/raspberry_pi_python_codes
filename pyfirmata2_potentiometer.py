from pyfirmata2 import Arduino
from time import sleep

if __name__ == "__main__":
    board = Arduino('my port here')
    print("Communication has started!")

    samplingRate = 100 # 100 Hz, tbm pode ser 10 Hz
    board.samplingOn(1000 / samplingRate) # o normal eh 19ms, aqui pus 10ms
    potentiometer = board.analog[2]

    def callBack(data):
        global potentiometer
        data = potentiometer.read()
        
    potentiometer.register_callback(callBack)
    potentiometer.enable_reporting()

    #####druga opcja
    samplingRate = 100 # 100 Hz, tbm pode ser 10 Hz
    board.samplingOn(1000 / samplingRate) # o normal eh 19ms, aqui pus 10ms
    potentiometer = board.analog[2]
    potentiometer.enable_reporting()

    while True:
        try:
            data = potentiometer.read()
            print(data)
            sleep(0.1)

        except KeyboardInterrupt:
            board.exit()
            potentiometer.disable_reporting()
