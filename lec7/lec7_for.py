for i in range(4):
    print(i)

for i in range(7):
    print("*" * i)

for i in range(1,10):
    for j in range(2,10):
        print(str(j) + " × " + str(i) + " = " + str(i * j), end= " ")
    print()