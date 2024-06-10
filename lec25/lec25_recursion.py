def downup(w): 
    print(w)
    if len(w) <= 1:
        return
    # Recursive call
    downup(w[:-1])
    print(w)

print(downup("Hello"))


# 시험 문제 예상
def to_radix(n, b):
    if n < b:
        return str(n)
    s = to_radix(n // b, b)
    return s + str(n % b)
    
print(to_radix(10, 2))