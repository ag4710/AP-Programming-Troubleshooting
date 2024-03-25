from cs1robots import *

create_world(avenues = 5, streets = 5)

# create a robot with one beeper
hubo = Robot()
hubo.set_trace("blue")

# move one step forward
# hubo.move()

# turn left 90 degress
# hubo.turn_left()

def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def move_num(num):
    for _ in range(num):
        hubo.move()

for _ in range(4):
    move_num(4)
    hubo.turn_left()
