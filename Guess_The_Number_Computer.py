import random

def guess(x):
    random_number = random.randint(1, x)
    print(f'Welcome to Number Guessing Game, range is 1 to {x}')

    guess = 0  # some adjustment to enter the loop first

    while (guess != random_number):
        guess = int(input('guess: '))
        if guess == random_number:
            print('Congratulations! that was a correct guess')
            break
        elif guess < random_number:
            print('Sorry! guess again, too low')
        else:
            print('Sorry! guess again, too high')

guess(20)

