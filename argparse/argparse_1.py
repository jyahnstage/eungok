import argparse
import math
import numpy as np

def circle_4(a, b=math.pi):
    big = a*a*b
    long = 2*a*b
    return big, long

def parsing_argument():
    parser = argparse.ArgumentParser(description='Process some Arguments Parsing',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    #positional arguments
    parser.add_argument(
        'title',
        metavar='문자열',
        type=str,
        help="write your message at positional arguments"
    )
    parser.add_argument(
        'radius',
        metavar='숫자',
        type=int,
        help="write radius of circle"
    )
    args = parser.parse_args()
    return args

def main():
    args = parsing_argument()
    print('지금 실행하는 코드는 argparse 기초 1입니다.')
    print(f'원의 반지름을 옵션으로 받아서 {args.title}를 구합니다.')
    big, long = circle_4(args.radius)
    print(f'원의 넓이: {big}, 둘레의 길이: {long}')

main()




