from cs1robots import *

load_world("./2_2/worlds/amazing2.wld")

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
    if hubo.right_is_clear():
        # Keep to the right
        turn_right()
    if hubo.front_is_clear():
        # move following the right wall
        hubo.move()
    else:
        # follow the wall
        hubo.turn_left()

# end of definitions, begin solution

hubo.drop_beeper()

while True:
    move_or_turn()
    if hubo.on_beeper(): 
        hubo.pick_beeper()
        break
    
