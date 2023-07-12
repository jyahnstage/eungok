#람다 표현식에 조건부 표현식 사용하기
# lambda 매개변수들: 식1 if 조건식 else 식2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_data = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(list_data)

list_data_1 = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
print(list_data_1)

#맵에 객체를 여러 개 넣기

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
c = list(map(lambda x, y: x * y, a, b))
print(c)

#filter 사용하기
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list_data_3 = list(filter(lambda x: x > 5 and x < 10, a))
print(list_data_3)

#reduce 사용하기
a = [1, 2, 3, 4, 5]
from functools import reduce
list_data_4 = reduce(lambda x, y : x + y, a)
print(list_data_4)