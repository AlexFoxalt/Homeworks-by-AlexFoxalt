def small_game():
    answer = input('I chose a random number (1:100) for you.\n Try to guess it: ')
    answer = int_check(answer)
    if not answer:
        print('!Error! Incorrect data.')
        small_game()
    print(f'Your number is "{answer}" and my number is\n...\n...\n...\n!!!{secret_number}!!! ')
    if answer == secret_number:
        restart_answer = input("!!!GREAT JOB!!! Houdini, is is you? Nevermind... Let's do it one more time?(Y): ")
        if restart_answer.upper() == 'Y':
            big_game()
        else:
            sys.exit()
    elif answer != secret_number:
        restart_answer = input("I'm sorry, but not this time... Do you want one more chance?(Y/N): ")
        if restart_answer.upper() == 'Y':
            small_game()
