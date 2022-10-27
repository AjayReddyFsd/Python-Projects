import random

def guess(x): #x is the upper limit of guesses
    start = 1
    end = x

    user_input = 0 # some adjustment to enter the loop first

    while user_input != 'y':
        guess = random.randint(start, end)
        print(f"guess = {guess}")

        user_input = input("""enter 'c' if correct, 'h' to guess higher and 'l' to guess lower: """)
        if user_input == 'c':
            print('yay, now i can read your mind too')
            break
        elif user_input == 'h':
            start = guess+1
        else:
            end = guess-1

guess(20)