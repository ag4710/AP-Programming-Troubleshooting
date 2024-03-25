from cs1robots import *

create_world()

# create a robot with one beeper
hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def move_num(num):
    for _ in range(num):
        hubo.move()

def move_or_turn():
    global num
    if hubo.front_is_clear(): 
        hubo.move()
    else:
        hubo.turn_left()
        num = num + 1

num = 0

while (num != 4):
    move_or_turn()
