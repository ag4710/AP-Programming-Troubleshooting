from cs1robots import *
import time

create_world(avenues = 5, streets = 5)
sleep_time = 0.5

hubo = Robot("yellow") 
time.sleep(sleep_time)
hubo.move()
ami = hubo
time.sleep(sleep_time)
ami.turn_left() 
hubo.move()

time.sleep(sleep_time)
hubo = Robot("blue") 
time.sleep(sleep_time)
hubo.move() 
time.sleep(sleep_time)
ami.turn_left() 
time.sleep(sleep_time)
ami.move()