f = open("lec20/planets.txt", "r")
s = f.readlines()
print(s, len(s))
for l in f:
    s = l.strip()
    print(s, end = " ")
f.close()