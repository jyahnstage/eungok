str = "Hello World"

for i in range(0, len(str)):
    print(f'{str[i]}_', end=" ")

# 문자열 대문자로 변경하는 함수 (string.upper)
s1 = "RICH"
s2 = s1.lower()
print(s2)

# 문자열 소문자로 변경하는 함수 (string.lower)
s1 = "rich"
s2 = s1.upper()
print(s2)

# 문자가 대문자인지 확인하는 함수 (string.isupper)
s1 = "Rich"
s2 = s1.isupper()
print(s2)

# 문자가 소문자인지 확인하는 함수 (string.islower)
s1 = "rich"
s2 = s1.islower()
print(s2)

#문자의 첫 문자를 대문자로 바꿔줌 (string.title)
s1 = "rich"
s2 = s1.title()
print(s2)

# 대문자는 소문자로, 소문자는 대문자로 바꿔줌 (string.swapcase)
print(s2.swapcase())

#replace 특정 단어를 다른 단어로 치환
a = "Hello World"
b = a.replace("Hello", "Hi")
print(b)

#split 문자열을 분리해서 리스트로 만들어 준다.

c = a.split("o")
print(c)

c = a.split(" ")
print(c)

a = "H e l l o W o r l d"
c = a.split(sep=" ", maxsplit=2)
print(c)
c = a.split(" ", maxsplit=-1)
print(c)

#splitlines()
str ='''안녕하세요.
반갑습니다.
어서오세요.
'''
result = str.splitlines()
print(result)