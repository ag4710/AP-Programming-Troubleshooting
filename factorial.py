# 팩토리얼 구현

def factorial(n):
    total = 1
    if n == 0:
        return total
    for i in range (1,n+1):
        total = total * i
    return total

def recursive_factorial(n):
    if n == 0:
        return 1
    total = n * recursive_factorial(n-1)
    n = n-1
    return total

number = int(input())
print(factorial(number))
print(recursive_factorial(number))