# shallow copy error

import random

def print_2d_list():
    for i in range(n):
        for j in range(m):
            print(table[i][j], end=" ")
        print()

n, m = map(int, input("책상 배치를 입력해주세요: ").split())
table = [[None] * n] * m

student = int(input("학생 수를 입력해주세요: "))
student_list = []

for i in range(student):
    student_list.append(i + 1)

for i in range(n):
    for j in range(m):
        print(i, end=" ")
        print(j)
        select = random.sample(student_list, 1)
        student_list.remove(select[0])
        table[i][j] = select[0]
        print_2d_list()
