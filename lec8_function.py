import math

degrees = 45

radians = degrees / 360.0 * 2 * math.pi
print(math.sin(radians)) 
print(math.sqrt(2) / 2)

sin = math.sin
pi = math.pi
radians = degrees / 360.0 * 2 * pi
print(sin(radians))

def compute_interest(amount, rate, years):
    value = amount * (1 + rate/100.0) ** years
    return value

s1 = compute_interest(200, 7, 1)
s2 = compute_interest(500, 1, 20)

print(s1)
print(s2)

x = float(input())
y = float(input())

# is integer a divisible by b?
def is_divisible(a, b):
    return a % b == 0

if is_divisible(x, y): 
    print('x is divisible by y')
else:
    print('x is not divisible by y')