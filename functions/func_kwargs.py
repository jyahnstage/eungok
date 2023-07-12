#키워드매개변수는 딕셔너리로 나오므로 원래 딕셔너리를 for문돌리면 key값만 나오니까 value를 넣어줘서 원하는 숫자를 나열하면 다 더하는 함수를 만듦

def keyword_함수(**kwargs):
    print(type(kwargs))
    num = 0
    print(kwargs.values())
    for i in kwargs.values():
        num = num + i

    return num
result = keyword_함수(a=1, b=5, c=6)      
print(result)

def name_hello_함수(**kwargs):
    print(type(kwargs))
    # for i in kwargs:
    #     print(type(i))
    #     print(f'{kwargs[i]}님 안녕하세요') 
        #  => 이렇게 해도 되지만 아래처럼 하는게 더 좋은 방법임.
    for i in kwargs.values():
        print(type(i))
        print(f'{i}님 안녕하세요')

name_hello_함수(a="안지영", b="안지2", c="안지3")      
