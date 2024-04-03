from cs1robots import *

a = 17
def test(): 
    # print(a) 지역 변수 a라 인식, 주어진 a가 없으니 에러 메시지 출력
    a = 13
    print(a)
test()

create_world(avenues = 5, streets = 5)
hubo = Robot()
hubo_direction = 0

def turn_left(): 
    hubo.turn_left() 
    global hubo_direction

    hubo_direction += 90

def turn_right():
    for i in range(3): 
        hubo.turn_left()
    global hubo_direction
    hubo_direction -= 90

a = "Letter a"
def f(a): 
    print("A = ", a)

def g():
    a = 7
    f(a + 1)
    print("A = ", a)

print("A = ", a)
f(3.14)
print("A = ", a)
g()
print("A = ", a)