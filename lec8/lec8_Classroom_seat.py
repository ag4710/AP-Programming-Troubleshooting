import random

# 2차원 배열 출력
def print_2d_list(table):
    for i in range(n):
        for j in range(m):
            print(table[i][j], end=" ")
        print()

# 자리 배치
def seating_arrangement(output_seat,student):
    total = n * m
    empty_seats = total - len(student)

    # 학생 수가 자리보다 많을 때
    if empty_seats < 0:
        over_student = True
        print("학생 수가 자리보다 많습니다.")
    
    for i in range(n):
        for j in range(m):
            # 학생 수가 자리보다 적을 때
            if not student:
                print("학생 수가 자리보다 적습니다.")
                print_2d_list(output_seat)
                print(f"{empty_seats}개의 자리가 남았습니다.")
                return output_seat
            
            select = random.sample(student, 1)
            student.remove(select[0])
            output_seat[i][j] = select[0]
    
    print_2d_list(output_seat)
    
    # 자리 없는 학생의 번호 출력
    if over_student:
        for i in student:
            print(i, end= " ")
        print("번 학생의 자리가 없습니다.")
    
    return output_seat

# 책상 입력 받기
n, m = map(int, input("책상 배치를 입력해주세요: ").split())
seat = [[0] * n for _ in range(m)]

# 학생 수 입력 받기
student = int(input("학생 수를 입력해주세요: "))
student_list = []
for i in range(student):
    student_list.append(i + 1)

# 실행
seat = seating_arrangement(seat, student_list)