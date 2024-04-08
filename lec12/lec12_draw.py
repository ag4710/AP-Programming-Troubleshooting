from cs1graphics import *
import time

canvas = Canvas(400, 300)
canvas.setBackgroundColor("light blue")
canvas.setTitle("CS101 Drawing exercise")

sq = Square(100)
canvas.add(sq)
sq.setFillColor("blue")
sq.setBorderColor("red")
sq.setBorderWidth(5)
sq.moveTo(200, 200)

for i in range(100):
    sq.move(1, 0)

    time.sleep(0.1)

r = Rectangle(150, 75) 
canvas.add(r)
r.setFillColor("yellow") 
r.moveTo(280, 150)

time.sleep(0.5)

#깊이 변경
sq.setDepth(10) 
r.setDepth(20)

time.sleep(0.5)

#회전
sq.rotate(45)

time.sleep(0.5)

#크기 조절
sq.scale(1.5)
r.scale(0.5)

time.sleep(0.5)

#Fade-out
for i in range(80): 
    sq.scale(0.95)
canvas.remove(sq)