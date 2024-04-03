from cs1graphics import *

def create_sun(radius = 30, color = "yellow"): 
    sun = Circle(radius) 
    sun.setFillColor(color) 
    sun.setBorderColor(color)
    sun.moveTo(100, 100)
    return sun

moon = create_sun(28, "gray")
star = create_sun(2) # create_sun(2, "yellow")과 동일
sun = create_sun() # create_sun(30,"yellow")과 동일