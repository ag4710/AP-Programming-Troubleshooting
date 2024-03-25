from cs1robots import *

create_world()

# create a robot with one beeper
hubo = Robot(beepers = 1)
hubo.set_trace("blue")

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def move_num(num):
    for _ in range(num):
        hubo.move()

def move_or_turn():
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()


hubo.drop_beeper()
hubo.move()

while not hubo.on_beeper():
    move_or_turn()
    if hubo.on_beeper(): 
        hubo.pick_beeper()
        break
    
