import random
import numpy

# 2차원 배열 출력
def print_2d_list(table):
    for i in table:
        for j in i:
            print(j, end=" ")
        print()

# 자리 배치
def seating_arrangement(output_seat,student):
    over_student = False
    total = horizontality * Perpendicular
    empty_seats = total - len(student_list)
    index = 0

    # 학생 수가 자리보다 많을 때
    if empty_seats < 0:
        over_student = True
        print("학생 수가 자리보다 많습니다.")
    
    for i in range(Perpendicular):
        for j in range(horizontality):
            select = student[index]
            if select == 0:
                output_seat[i][j] = select
                index = index + 1
            else:
                output_seat[i][j] = select
                index = index + 1
                student_list.remove(select)
    
    # 학생 수가 자리보다 적을 때
    if not student_list:
        print("학생 수가 자리보다 적습니다.")
        print_2d_list(output_seat)
        print(f"{empty_seats}개의 자리가 남았습니다.")

        return output_seat
    
    print_2d_list(output_seat)

    # 자리 없는 학생의 번호 출력
    if over_student:
        for i in student_list:
            print(i, end= " ")
        print("번 학생의 자리가 없습니다.")
    
    return output_seat

# 책상 입력 받기
def desk_arrangement():
    global horizontality, Perpendicular, seat
    horizontality, Perpendicular = map(int, input("책상 배치를 입력해주세요: ").split())
    seat = [[None] * horizontality for _ in range(Perpendicular)]

# 학생 수 입력 받기
def number_of_students():
    global student_list
    student = int(input("학생 수를 입력해주세요: "))
    student_list = []
    for i in range(student):
        student_list.append(i + 1)
    return student_list

# 학생 순서 랜덤 돌리기
def shuffle_student(input_list):
    if (horizontality * Perpendicular) > len(input_list):
        for _ in range((horizontality * Perpendicular) - len(input_list)):
            input_list.append(0)

    random.shuffle(input_list)

# 실행
desk_arrangement()
list_student = number_of_students().copy()
shuffle_student(list_student)
seat = seating_arrangement(seat, list_student)