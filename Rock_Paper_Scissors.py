import random

def rockPaperScissors():
    while(True):
        computer = random.choice(['r', 'p', 's'])
        user = input("""enter 'r' for rock, 'p' for paper and 's' for scissors: """)

        if(computer == user):
            print('tie')
            print(f'computer = {computer} & user = {user}')
            continue
        elif((computer == 'r' and user == 's')or(computer == 's' and user == 'p')or(computer == 'p' and user == 'r')):
            print('yippe, I won')
            print(f'computer = {computer} & user = {user}')
            break
        else:
            print('congrats, U won')
            print(f'computer = {computer} & user = {user}')
            break

rockPaperScissors()




