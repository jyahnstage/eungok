#딕셔너리는 immutable불변 하는 key 값: mutable 변할 수 있는 value값으로 이루어짐
# immutable ex) int, tuple, float, boolean
# mutable ex) list, 집합{}, dict 등
#O
a = {1: 5, 2: 3}
a1 = {(1,5): 5, (3,3): 3}
a2 = {3.6: 5, "abc": 3}
a3 = {True: 5, "abc": 3}

#X
# a4 = {{1, 3}: 5, {3, 5}: 3}
# a5 = {[1, 2]: 5, [3, 4]: 3}
# a6 = {{'a': 1}: 5, {'b': 2}: 3}

# 값은 중복될 수 있으나 중복되면 맨 마지막값으로 덮어씌워짐
a7 = {'a': 1, 'a': 2}
#=> a = {'a': 2}


#keys(), values(), items()
print(a.keys())
#=> dict_keys([1, 2])
print(a.values())
#=> dict_values([5, 3])
print(a.items())
#=>dict_items([(1, 5), (2, 3)])

#튜플 또는 리스트로 이루어진 걸 dict로 만들기
result = dict([('a', 1), ('b', 2), ('c', 3)])
print(result)
#=> {'a': 1, 'b': 2, 'c': 3}

name_and_ages = [['alice', 5], ['Bob', 13]]

dict(name_and_ages)
{'alice': 5, 'Bob': 13}

name_and_ages = [('alice', 5), ('Bob', 13)]

dict(name_and_ages)
{'alice': 5, 'Bob': 13}

name_and_ages = (('alice', 5), ('Bob', 13))

dict(name_and_ages)
{'alice': 5, 'Bob': 13}

name_and_ages = (['alice', 5], ['Bob', 13])

dict(name_and_ages)
{'alice': 5, 'Bob': 13}


#새로운 키와 밸류 추가하기
result['name']= 'jya'
print(result)
#=> {'a': 1, 'b': 2, 'c': 3, 'name': 'jya'}

#수정하기 update
u = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
u.update({'bob':90, 'tony':99, 'kim':30})
print(u)
# => u = {'alice': [1, 2, 3], 'bob': 90, 'tony': 99, 'suzy': 30, 'kim': 30}

#이렇게도 딕셔너리 선언할 수 있음
d = dict(alice = 5, bob = 20, tony = 15, suzy = 30)
print(d)
d = {'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}

#dictionary for 문
# 딕셔너리를 for 문으로 돌리면 key값이 할당됨. 단 순서는 보장할 수 없음.

for i in d:
    print(i)

# alice
# bob
# tony
# suzy

# for문에서 value 값 호출하려면 values() 사용.
for j in d.values():
    print(j)
# 5
# 20
# 15
# 30

#key 와 value를 한번에 for문에서 나오게하려면 items() 사용.
for k in d.items():
    print(k)
print('----------')

# ('alice', 5)
# ('bob', 20)
# ('tony', 15)
# ('suzy', 30)

# key_list = list(d.keys())
# print(key_list)

# value_list = list(d.values())
# print(value_list)

key_list = []
value_list = []

for key, value in d.items():
    key_list.append(key)
    value_list.append(value)

print(key_list)
print(value_list)

#del, pop