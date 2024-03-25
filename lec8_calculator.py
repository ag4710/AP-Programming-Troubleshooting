def calculator(OperationSymbol):
    if OperationSymbol == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif OperationSymbol == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif OperationSymbol == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif OperationSymbol == '/':
        print(f"{num1} / {num2} = {num1 / num2}")
    elif OperationSymbol == '//':
        print(f"{num1} // {num2} = {num1 // num2}")
    elif OperationSymbol == '%':
        print(f"{num1} % {num2} = {num1 % num2}")
    elif OperationSymbol == '**':
        print(f"{num1} ** {num2} = {num1 ** num2}")
    else:
        print("연산 기호를 입력해주세요 ㅠㅠ")


def request_calulator():
    global num1, num2
    num1 = float(input())
    num2 = float(input())
    user_OperationSymbol = input()
    return user_OperationSymbol

calculator(request_calulator())
