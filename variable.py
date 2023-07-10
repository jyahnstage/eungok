a = 10
b = "Hello"

print(type(a))
print(type(b))

a = True
print(type(a))

a = b = c = 10
d, e, f = 10, 3.14, "test"

print(a,b,c)
print(d,e,f)

str = "안녕하세요!!! '김태경'"
str_literal = '''
fwefwefwefwe \n
fwefwefwe \n
fwefwefwe \n
fwefwefwefwefwe \n
'''

print(str)
print(str_literal)

test = '안녕하세요!! "너"'
print(test)

# 리터럴 표기 방법
name = "안지영"
literal_1 = "안녕하세요!!!" + name
print(literal_1)

literal_2 = f"안녕하세요 {name} fewfew"
print(literal_2)