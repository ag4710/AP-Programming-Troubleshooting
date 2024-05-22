f  = open("lec20/planets.txt", "r")
current = 0
earth = 0
for line in f:
    current += 1
    planet = line.strip().lower()
    if planet == "earth":
        earth = current
print("Earth is planet #%d" % earth)

for x in range(2):
    for y in range(5):
        print(y, end = " ")
        if y == 3:
            break