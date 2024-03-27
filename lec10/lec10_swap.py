def swap(a, b):
    a, b = b, a
    print(f"a: {a}, b: {b}")

x, y = 123, 456
swap(x, y) 
print(f"x: {x}, y: {y}")