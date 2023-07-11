# for i in range(5):
#     print(i)

# for i in range(2, 20):
#     print(i)

# for i in range (0, 20, 3):
#     print(i)


# 짝수의 합 구하기 ( 두 가지 다 되는데 앞에거는 누적 숫자가 다 표시됨 ㅋㅋ)

sum = 0
for i in range(0, 101, 2):
    sum += i
    print(sum)

# sum = 0
# for i in range(1, 101):
#     if i % 2 == 1:
#         continue
#     sum += i

# print("짝수의 합: ", sum)