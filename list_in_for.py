# [표현식 for 항목 in 리스트 or 튜플 if 조건문]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list = [num * 3 for num in list]
# print(list)
# list = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# list = [num * 3 for num in list if num % 2 == 1]
# print(list)
# list = [3, 9, 15, 21, 27]

list = [num * 3 for num in list if num % 2 == 0]
print(list)
list = [6, 12, 18, 24, 30]