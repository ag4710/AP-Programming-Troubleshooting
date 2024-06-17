## 클래스와 함수 선언 부분 ##
def noMidQuickSort(ary):
    n = len(ary)
    if n <= 1:           # 정렬한 리스트의 개수가 1개 이하면
        return ary

    pivot = ary[n//2]    # 기준 값을 중간값으로 지정
    leftAry, rightAry = [], []

    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
    
    return noMidQuickSort(leftAry) + [pivot] + noMidQuickSort(rightAry)

def quickSort(ary):
    n = len(ary)
    if n <= 1:           # 정렬한 리스트의 개수가 1개 이하면
        return ary

    pivot = ary[n//2]    # 기준 값을 중간값으로 지정
    leftAry, midAry, rightAry = [], [], []

    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
        else:
            midAry.append(num)
    
    return quickSort(leftAry) + midAry + quickSort(rightAry)


## 전역 변수 선언 부분 ##
dataAry = [188, 162, 168, 120, 50, 150, 177, 105]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 -->', dataAry)