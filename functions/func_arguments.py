#a, b, c 매개변수
def multiple_add(alpha, beta, gama):
    num = alpha * beta + gama
    return num

#a, b, c 위치 인자로 전달
result = multiple_add(2, 3, 4)
print(result)

#a, b, c를 키워드 인자로 전달
result_keywords = multiple_add(alpha=2, beta=3, gama=4)
print(result_keywords)

#키워드 인자는 위치를 바꿔도 된다
result_keywords_1 = multiple_add(gama=4, alpha=2, beta=3)
print(result_keywords_1)

#위치 인자부터 먼저 호출하고 나중에 키워드 인자를 호출한다.
result_keywords_2 = multiple_add(2,3, gama=4)
print(result_keywords_2)

#매개변수 키워드값을 부여하면 인자값으로 전달 받지 않아도 된다.
def multiple_add_keywords(alpha, beta, gama=100):
    num = alpha * beta + gama
    return num

result_keywords3 = multiple_add_keywords(10, 20)
print(result_keywords3)

result_keywords4 = multiple_add_keywords(gama=10, alpha=20, beta=500)
print(result_keywords4)

result_keywords5 = multiple_add_keywords(alpha=10, beta=500)
print(result_keywords5)