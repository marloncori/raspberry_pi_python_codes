#!/usr/bin/env python
import RPi.GPIO as pine64
from time import sleep

def run_test():
  led_1 = 71
  led_2 = 76
  sensor = 64

  pine64.setmode(pine64.BCM)

  pine64.setup(led_1, pine64.OUT, initial=pine64.HIGH)
  pine64.setup(led_2, pine64.OUT, initial=pine64.LOW)
  pine64.setup(sensor, pine64.IN, pull_up_down=pine64.HIGH)
  
  print("\n=================================================")
  print("    Starting obstacle detection program...")
  sleep(1)
  
  if bool(pine64.input(sensor)):
    print("\n------------------------------------------------")
    print("\t Object has been detected!!!")
    pine64.output(led_1, pine64.LOW)
    pine64.output(led_2, pine64.HIGH)
    print("\n------------------------------------------------")
    sleep(1)
    
  else:    
    print("\n------------------------------------------------")
    print("\t No object has been spotted up to now.")
    pine64.output(led_1, pine64.HIGH)
    pine64.output(led_2, pine64.LOW)
    print("\n------------------------------------------------")
    sleep(1)

if __name__ == '__main__':
  try:
    
    while true:
      run_test()
      
  except KeyboardInterrupt:
    print("\n\n Program has been terminated. Goodbye!")
    pine64.cleanup()
