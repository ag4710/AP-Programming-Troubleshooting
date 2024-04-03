def avg(data, start = 0, end = None): 
    if not end: # (not None)==True, (not 4)==False
        end = len(data)
    return sum(data[start:end]) / float(end-start)

d = (3, 4, 5, 6, 7)
print(avg(d, 1, 4))
print(avg(d, 2)) # avg(d,2,None) 또는 avg(d,2,5) 와 동일
print(avg(d))

print(avg(d, end=3))
print(avg(data=d, end=3))
print(avg(end=3, data=d))
