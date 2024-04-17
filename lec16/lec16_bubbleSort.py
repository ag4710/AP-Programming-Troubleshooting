def bubbleSort(a):
    sorted = False
    while (not sorted):
        sorted = True
        for i in range(1,len(a)):
            if(a[i-1] > a[i]):
                a[i-1], a[i] = a[i], a[i-1]
                sorted = False

def for_bubbleSort(b):
    for j in range(len(b)-1):
        for i in range(1,len(b)-j):
            if(b[i-1] > b[i]):
                    b[i-1], b[i] = b[i], b[i-1]

case1 = [5,1,4,2,8]
for_bubbleSort(case1)
print(case1)

case2 = [5,1,4,2,8]
bubbleSort(case2)
print(case2)