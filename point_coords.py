from time import sleep
import math


params = []
xq = 0.0
yq = 0.0

def adorn(second=False):
    if(bool(second)):
        print("\033[1;33m=\033[0m" * 44)
        print("\033[1;30m          K I N E M A T I C S\033[0m")
        print("\033[1;33m=\033[0m" * 44)
    else:
        print("\033[1;33m=\033[0m" * 44)
        print("\033[1;30m          E N D   O F  P R O G R A M\033[0m")
        print("\033[1;33m=\033[0m" * 44)
              
def gather_data():
    adorn(True)
    print("\033[1;34mLet us start the point kinematics application!\033[0m")
    l1 = float(input("\033[1;35m\n Please enter the length of the first link: \033[0m"))
    l2 = float(input("\033[1;36m Now please enter the length of the second link: \033[0m"))
    th1 = float(input("\033[1;35m And now provide us with the first angle value: \033[0m"))
    th2 = float(input("\033[1;36m Then tell us the value of the second angle: \033[0m"))
    params = [l1, l2, th1, th2]
    return params

def x_coord(values):
    print("\033[1;30m   ==> Calculating...\033[0m")
    sleep(2)
    l1 = values[0]
    l2 = values[1]
    th1 = values[2]
    th2 = values[3]
    x = l1 * math.cos(th1) + l2 * math.cos(th1 + th2)
    return x

def y_coord(values):
    l1 = values[0]
    l2 = values[1]
    th1 = values[2]
    th2 = values[3]
    y = l1 * math.sin(th1) + l2 * math.sin(th1 + th2)
    return y

def show_position(xq, yq):
    sleep(1)
    print("\033[1;34m\n The coordinates of point Q are: \033[0m \033[1;31m\n\t x: {:.2f}\033[1;32m\n\t y: {:.2f}\n\033[0m".format(xq, yq))
    adorn()
              
if __name__ == '__main__':
    try:
        params = gather_data()
        xq = x_coord(params)
        yq = y_coord(params)
        show_position(xq, yq)

    except KeyboardInterrupt:
        print(" User stooped the application. Goodbye!")