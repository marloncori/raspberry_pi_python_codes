from pyfirmata2 import Arduino, util
from time import sleep

if __name__ == "__main__":
    uno = Arduino("COM9")
    print("Communication has started")

    it = util.Iterator(uno)
    it.start()

    potent = uno.analog[0]
    potent.enable_reporting()

    while True:
        print(potent.read())
        sleep(0.1)
