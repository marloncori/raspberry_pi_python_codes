from time import sleep

space = "\t"
msg = "Test."

for i in range(0, len(msg)):
    print(msg)
    msg = space + msg
    sleep(1)
