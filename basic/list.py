a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ('Life', 'is')]
f = [1, 2, ['Life', 'is']]

g = [1, 2, 3]
h = [4, 5]

# g + h = [1,2,3,4,5]

# g * 3 = [1,2,3,1,2,3,1,2,3]

#리스트 값 수정하기
a = [1, 2, 3]
a[2] = 4
a = [1, 2, 4]

#del 함수를 사용해 리스트 요소 삭제하기

del a[1]
print(a) # = [1, 4]

#remove로 삭제하기

a.remove(1)
print(a) # = [4]

#pop 괄호안에 안쓰면 맨 뒤에 요소부터 삭제함. 괄호 안에 숫자쓰면 인덱스로 세서 삭제함.
z = [1, 2, 'a']
z.pop()
print(z.pop())
print(z)


# 추가. append, insert, extend
z.append(5)
print(z)

z.insert(0,6)
print(z)

z.extend([4,7])
print(z)

#sort (*, key=None, reverse=False)
#sorted (iterable, /, *, key=None, reverse=False)
s = [2, 3, 5, 1, 6, 4]
# s.sort()
# print(s)
s.sort(reverse=True)
print(s)

s3 = sorted([1, 4, 6, 3])
print(s3)
s4 = sorted(s, reverse=True)
print(s4)

#key
'''정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.
key 값을 기준으로 정렬되고 기본값은 오름차순이다.'''

str_list = ['좋은하루','good_morning','굿모닝','niceday']
print(sorted(str_list, key=len))
print(sorted(str_list, key=len, reverse=True))

#reverse

r = ['a', 'c', 'b']
r.reverse()
print(r)
r2 = [1, 2, 3, 'a', 'c', 'b', 'a' ]
r2.reverse()
print(r2)

#index
print(r.index('a')) #=> 2

#count
print(r2.count('a'))

#clear
r2.clear()
print(r2)

r2.append(5)
r2.extend([3, 4])
print(r2)
r2.append([3,4])
print(r2)

r2.insert(2, [7,8])
print(r2)