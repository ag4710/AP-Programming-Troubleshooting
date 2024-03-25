def graph(point1, point2):
    x_change = point1[0] - point2[0]
    y_change = point1[1] - point2[1]
    inclination = y_change / x_change
    y_intercept = inclination * point2[0]
    print(f"기울기는 {inclination}")
    print(f"y 절편은 {point2[1] - y_intercept}")

    
dot1_x, dot1_y= map(float, input("첫 번째 점의 좌표를 적어주세요: ").split())
input_point1 = (dot1_x, dot1_y)
dot2_x, dot2_y = map(float, input("두 번째 점의 좌표를 적어주세요: ").split())
input_point2 = (dot2_x, dot2_y)

graph(input_point1, input_point2)