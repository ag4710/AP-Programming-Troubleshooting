x0 = 1
x1 = 2
x2 = 3
val = 1.99999

print("Max between " + str(x0) + " and " + str(x1) + " is " + str(val))
print("Max between %d and %d is %g" % (x0, x1, val))
print("%3d~%3d:%10g" % (x0, x1, x2))
print("%-3d~%-3d:%-12g" % (x0, x1, x2))  # 왼쪽 정렬

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False 
    return True

print("abc" in "01234abcdefg" )
print("abce" in "01234abcdefg")
dol = '123456'
print(dol.join("python"))