import random 
import time

def simple_sort(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if i<j and li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    return li

def merge_sort(li):
    if len(li)<=1:
        return li
    m=len(li)//2
    l1=merge_sort(li[:m])
    l2=merge_sort(li[m:])
    new_li=[]
    i,j=0,0
    return 

def quick_sort(li):
    if len(li)<=1:
        return li
    pivot=li[0]
    left,right=[],[]
    for i in range(1,len(li)):
        if li[i]<pivot:
            left.append(li[i])
        else:
            right.append(li[i])
    return quick_sort(left)+[pivot]+quick_sort(right)

large_list = list(range(20000)) 
random.shuffle(large_list)
st = time.time()
large_list=quick_sort(large_list)
print("Running time: %f sec" % (time.time() - st))