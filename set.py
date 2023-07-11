s1 = set([1, 2, 2, 2, 2, 2, 3])
print(s1)
s1 = {1, 2, 3}

s2 = set("Hello World")
print(s2)
s2 = {'H', 'o', 'e', 'W', 'd', ' ', 'l', 'r'}

s3 = list("Hello World")
print(s3)
s3 = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

s4 = tuple("Hello World")
print(s4)
s4 = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
print(s1 & s2)
# = {4, 5, 6}

print(s1.intersection(s2))
# = {4, 5, 6}

#합집합
print(s1 | s2)
# = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(s1.union(s2))
# = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#차집합
print(s1 - s2)
# = {1, 2, 3}
print(s1.difference(s2))
# = {1, 2, 3}

#대칭차집합
print(s1 ^ s2)
# = {1, 2, 3, 7, 8, 9}
print(s1.symmetric_difference(s2))
# = {1, 2, 3, 7, 8, 9}

#원소 추가
s1.add(10)
print(s1)
# = {1, 2, 3, 4, 5, 6, 10}

s1.update([1, 2, 11, 12])
print(s1)
# = {1, 2, 3, 4, 5, 6, 10, 11, 12}

#remove
s1.remove(12)
print(s1)
# = {1, 2, 3, 4, 5, 6, 10, 11}