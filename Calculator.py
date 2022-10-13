def calculator():

    while True:
        user_choice = int(input('please enter 1 to add, 2 to subtract, 3 to mult, 4 to div and 0 to exit: '))

        if(user_choice == 0):
            print('sucessfully exited')
            break
        else:   
            a = float(input('please enter the value of a: '))
            b = float(input('please enter the value of b: '))

            if user_choice == 1:
                print(f'{a} + {b} = {a+b}')
            elif user_choice == 2:
                print(f'{a} - {b} = {a-b}')
            elif user_choice == 3:
                print(f'{a} * {b} = {a*b}')
            else:
                print(f'{a} / {b} = {a/b}')
            

calculator()