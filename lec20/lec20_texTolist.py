planets = []
f = open("lec20/planets.txt", "r")
#for line in f:
    #planets.append(line.strip())
planets = f.readlines()
f.close()
print(planets)

# planets = f.readlines()로 반복문을 대체할 수 있음