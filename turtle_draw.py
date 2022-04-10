from turtle import *
from time import sleep
from invalid_value import *

cnt = 0

def draw_shape(counter, F, L, B):
    counter = 0
    color('blue')
    begin_fill()
    if F == 0 or L == 0 or B == 0:
        raise InvalidValueError(" Values for F, B, R, L cannot be zero!")
    while counter < 27:
        forward(F)
        sleep(0.1)
        forward(F)
        sleep(0.1)
        left(L)
        sleep(0.1)
        left(L)
        sleep(0.1)
        backward(B)
        sleep(0.1)
        backward(B)
        sleep(0.1)
        if abs(pos()) < 1:
            break
        counter +=1

    end_fill()
    done()

def draw_more(counter, F, B, R, L):
    counter = 0
    color('blue')
    begin_fill()
    if F == 0 or B == 0:
        raise InvalidValueError(" Values for F, B, R, L cannot be zero!")
    while counter < 27:
        forward(F)
        sleep(0.1)
        forward(F)
        sleep(0.1)
        backward(B)
        sleep(0.1)
        backward(B)
        sleep(0.1)
        right(R)
        sleep(0.1)
        right(R)
        sleep(0.1)
        left(L)
        sleep(0.1)
        left(L)
        sleep(0.1)
        if abs(pos()) < 1:
            break
        counter +=1

    end_fill()
    done()
    
def draw_circle(ct, R, F, L, B):
    ct = 18
    if R == 0 or F == 0 or L == 0 or B == 0:
        raise InvalidValueError(" Values for F, B, R, L cannot be zero!")
    else:
        color('red')
        begin_fill()
        while ct > 0:
            backward(B)
            sleep(0.1)
            left(L)
            sleep(0.1)
            forward(F)
            sleep(0.1)
            right(R)
            sleep(0.1)
            backward(B)
            sleep(0.1)
            left(L)
            sleep(0.1)
            forward(F)
            sleep(0.1)
            right(R)
            sleep(0.1)
            if abs(pos()) < 1:
                break
            ct -=1
        end_fill()
        done()
    
if __name__ == '__main__':
    try:
        # upsidedown triangle
        # draw_shape(cnt, 40, 60, 80)
        # nine angles
        # draw_shape(cnt, 20, 40, 60)
        #draw_shape(cnt, 150, 300, 100)
        # 18 angles
        draw_more(cnt, 40, 90, 40, 90)
        draw_circle(cnt, 5, 10, 20, 30)
    except (KeyboardInterrupt, SystemExit):
        print("   User has stopped program execution")

