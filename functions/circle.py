import math

def circle_1(a, b=math.pi):
    print(f'원의 넓이는 {a*a*b}입니다.')

def circle_2(a, b=math.pi):
    print(f'원의 둘레의 길이는 {2*a*b}입니다.')

def circle_3(a, b=math.pi):
    print(f'원의 넓이는 {a*a*b}이고, 원의 둘레의 길이는 {2*a*b}입니다.')

def circle_4(a, b=math.pi):
    big = a*a*b
    long = 2*a*b
    return big, long

a = int(input("원의 반지름을 넣으세요"))
circle_1(a)
circle_2(a)
circle_3(a)
big, long = circle_4(a)
print(f'원의 넓이는 {big}이고 둘레의 길이는 {long}입니다.')

#다른 사람 코드
# def circle_square_round(a):
#     square = a*a*math.pi
#     round = 2*a*math.pi
#     return square, round
# a = int(input("반지름의 길이를 적으세요."))
# square, round =circle_square_round(a)
# print(f'square = {square}, round = {round}')
