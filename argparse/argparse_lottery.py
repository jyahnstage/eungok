import random
import argparse

class Lottery:
    def __init__(self, mymoney):
        self.my_money = mymoney

    def game(self):
        betting_money = int(input('how much do you want to bet? \t'))
        
        if  self.my_money < betting_money:
            print("돈이 부족합니다.")
            return
            
        else:
            choice = 1
            while choice:
                if self.my_money < betting_money:
                    print("game end")
                    choice = 0
                else:
                    select_num = int(input('choose a number between 1 and 6 \t'))
                    random_number = random.randint(1, 6)
                    if select_num != random_number:
                        print(f'your choicd: {select_num}, random number: {random_number}')
                        print('you lost')
                        self.my_money = self.my_money - betting_money
                        print(f'your current money: {self.my_money}')
                        select_game = input('continue? 1 or 2 \t')
                        if select_game == "1":
                            choice = 1
                        elif select_game == "2":
                            choice = 0
                            print("game end")
                    elif select_num == random_number:
                        print(f'your choicd: {select_num}, random number: {random_number}')
                        print('you won')
                        self.my_money = self.my_money + betting_money * 10
                        print(f'your current money: {self.my_money}')
                        select_game = input('continue? 1 or 2 \t')
                        if select_game == "yes":
                            choice = 1
                        elif select_game == "no":
                            choice = 0
                            print("game end")

# lottery = Lottery(10000)
# lottery.game()
def parsing_argument():
    parser = argparse.ArgumentParser(description='Sample for using argparse',
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    #positional arguments
    parser.add_argument(
        'amount',
        metavar='amount',
        type=int,
        nargs='+',
        help="How much money do you have?",
        default=0
    )
    
    args = parser.parse_args()
    return args

def main():
    args = parsing_argument()
    lottery = Lottery(args.amount[0])
    lottery.game()

main()
