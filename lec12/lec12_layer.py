from cs1graphics import *

canvas = Canvas(400, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("CS101 Drawing exercise")

car = Layer()
car.move(0,160)
canvas.add(car)

tire1 = Circle(10, Point(-20,-10))
tire1.setFillColor('black')
car.add(tire1)

tire2 = Circle(10, Point(20,-10))
tire2.setFillColor('black')
car.add(tire2)

body = Rectangle(70,30,Point(0,-25))
body.setFillColor('blue')
body.setDepth(60)
car.add(body)

for _ in range(50):
    car.move(2,0)
for _ in range(22):
    car.rotate(-1)
for _ in range(50):
    car.move(2,-1)
for _ in range(22):
    car.rotate(1)
for _ in range(50):
    car.move(2,0)
for _ in range(10):
    car.scale(1.05)
