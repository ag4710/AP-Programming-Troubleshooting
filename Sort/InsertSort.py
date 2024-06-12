## 클래스와 함수 선언 부분 ##
def findInsertIdx(ary, data):
    findIdx = -1
    for i in range(0, len(ary)):
        if (ary[i] > data):
            findIdx = i
            break
    if findIdx == -1:
        return len(ary)
    else:
        return findIdx

# testAry = []
# insPos = findInsertIdx(testAry, 55)
# print('삽입할 위치 -->', insPos)

# testAry = [33, 77, 88]
# insPos = findInsertIdx(testAry, 55)
# print('삽일할 위치 -->', insPos)

# testAry = [33, 55, 77, 88]
# insPos = findInsertIdx(testAry, 100)
# print('삽일할 위치 -->', insPos)

## 전역 변수 선언 부분 ##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 부분 ##
print('정렬 전 -->', before)
for i in range(len(before)):
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)
print('정렬 후 -->', after)


## 클래스와 함수 선언 부분 ##
def insertionSort(ary):
    n = len(ary)
    for end in range(1,n):
        for cur in range(end, 0, -1):
            if (ary[cur-1] > ary[cur]):
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
            
    return ary

## 전역 변수 선언 부분 ##
dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = insertionSort(dataAry)
print('정렬 후 -->', dataAry)