from cs1media import *

red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)

img = create_picture(100, 100, purple) 
img.show()
img.set_pixels(yellow)
img.show()
img.set(50, 50, (255, 0, 0))
img.show()