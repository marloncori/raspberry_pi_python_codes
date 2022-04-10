import time

def start_timer():
    ## events ###########
    interval = 0
    sensor_interval = 0
    battery_interval = 0
    ####################
    delay = 2
    reading_freq = 4
    checking_freq = 8
    ###################
    count = 0

    while count <= 40:
        now = time.time()
        if now >= interval:
            print( str(count) + " seconds have passed.")
            interval = now + delay
            count += 2
        
        now2 = time.time()        
        if now2 >= sensor_interval:
            print("\t Reading the sensors...") 
            sensor_interval = now2 + reading_freq
    
        now3 = time.time()        
        if now3 >= battery_interval:
            print("\t\t Checking battery status...") 
            battery_interval = now3 + checking_freq

if __name__ == '__main__':
    try:
        start_timer()
    except (KeyboardInterrupt, SystemExit):
        print(" User has stopped program execution.\n Goodbye!")
        

