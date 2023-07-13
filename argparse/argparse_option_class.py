import argparse

class Cat:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def __str__(self):
        return f'Cat(name={self.name}, color={self.color}, sound={self.sound})'
    
    def lotto(self):
        print(f'이름은 {self.name}이고, 색깔은 {self.color}의 고양이가 {self.sound}하고 웁니다.')

def parsing_argument():
    parser = argparse.ArgumentParser(description='Sample for using argparse',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    #positional arguments
    parser.add_argument(
        '-c',
        '--character',
        metavar='string',
        type=str,
        nargs='*',
        help="Give a cat a name, color, and sound.",
        default=["dongdong", "brown", "meow"]
    )
    
    args = parser.parse_args()
    print(args)
    return args
# parsing_argument()

def main():
    args = parsing_argument()
    cat = Cat(args.character[0], args.character[1], args.character[2])
    cat.lotto()


# main()   

# nabi = Cat("나비","흰색")
# nero = Cat("네로", "검은색")

# print(nabi)
# print(nero)