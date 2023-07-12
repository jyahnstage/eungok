def odd_sum():
    num = 0
    for i in range(11):
        if i % 2 == 0:
            continue
        num = num + i
    
    return num  #return 이후에는 실행되지 않음.
    print(f'0부터 10까지 dgdfh 합은 {num}입니다.')
    

# result = odd_sum()
# print(f'0부터 10까지 짝수의 합은 {result}입니다.')