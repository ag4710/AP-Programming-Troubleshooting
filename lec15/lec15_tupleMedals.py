medals = [
    ('Australia', 0, 2, 1), ('Austria', 4, 8, 5), ('Belarus', 5, 0, 1),
    ('Canada', 10, 10, 5), ('China', 3, 4, 2), ('Croatia', 0, 1, 0), 
    ('Czech Republic', 2, 4, 2), ('Finland', 1, 3, 1), ('France', 4, 4, 7), 
    ('Germany', 8, 6, 5), ('Great Britain', 1, 1, 2), ('Italy', 0, 2, 6), 
    ('Japan', 1, 4, 3), ('Kazakhstan', 0, 0, 1), ('Latvia', 0, 2, 2), 
    ('Netherlands', 8, 7, 9), ('Norway', 11, 5, 10), ('Poland', 4, 1, 1), 
    ('Russia', 13, 11, 9), ('Slovakia', 1, 0, 0), ('Slovenia', 2, 2, 4), 
    ('South Korea', 3, 3, 2), ('Sweden', 2, 7, 6), ('Switzerland', 6, 3, 2), 
    ('Ukraine', 1, 0, 1), ('United States', 9, 7, 12)
]

def print_totals1():
    for country, g, s, b in medals: 
        print(country + ":", g + s + b)

def print_totals2():
    for item in medals:
        print(item[0] + ":", sum(item[1:]))

def histogram(): 
    t = [0] * 13
    for item in medals:
        total = sum(item[1:])
        t[total // 3] += 1
    for i in range(13):
        print (str(3*i) + "~" + str(3*i+2)+":\t"+("*"* t[i]))

print_totals1()
print()
print_totals2()
print()
histogram()
