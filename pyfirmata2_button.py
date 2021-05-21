from pyfirmata2 import Arduino

PORT = Arduino.AUTODETECT
arduino = Arduino(PORT)
print("Setting up connection...")

arduino.samplingON()
#by default 19 millis

button = arduino.get_pin("d:6:i")
button.enable_reporting()

while True:
    
    strVal = button.read()
    if strVal == "True":
        print("Button pressed")

    elif strVal == "False":
        print("Button not pressed")

    else:
        print("Button has never been pressed")

    sleep(0.1)

arduino.exit()
