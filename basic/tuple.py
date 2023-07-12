t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab','cd'))

#인덱싱, 슬라이싱
print(t5[0])
print(t5[2][1])
print(t5[1:])
print(t5[0:2])
print('---------------')
print(t5[:2])
print(t5[-1])
print(t5[-2:])
print(t5[:-2])

print(len(t5))

for i in range(len(t5)):
    print("안녕하세요")

#tuple 더하기
t1 = (1,2,'a','b')
t2 = (3,4)
t3 = t1 + t2
print(t3)
t3 = (1, 2, 'a', 'b', 3, 4)

#tuple 곱하기
t4 = t1 * 3
print(t4)

print(tuple([1,2,3]))
