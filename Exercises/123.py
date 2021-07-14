def advanced_mid_game():
    bottom_range = top_range = ''
    number_of_attempts_desired = input("1. Enter the number of attempts that you wish (1:∞): ")
    number_of_attempts_desired = int_made(number_of_attempts_desired)
    if not number_of_attempts_desired:
        print("Incorrect data.")
        advanced_mid_game()
    elif number_of_attempts_desired == 1:
        print("Hm... you're a cocky dude. You have only 1 attempt!")
    else:
        print(f"You'll have {number_of_attempts_desired} attempts.")
    bottom_range = input("2. Enter the |bottom| of random number range (1:∞): ")
    top_range = input("3. Enter the |top| of random number range (*greater then previous number*): ")
    bottom_range = int_made(bottom_range)
    top_range = int_made(top_range)
    if not top_range or not bottom_range or bottom_range >= top_range:
        print("Incorrect data.")
        advanced_mid_game()
    print(bottom_range, top_range)

    top_range = int_made(top_range)
    if not top_range or bottom_range > top_range:
        print("Incorrect data.")
        advanced_mid_game()
    SECRET_NUMBER[0] = random.randint(bottom_range, top_range)
    # print('SECRET>>>', SECRET_NUMBER[0], '<<<SECRET')                      # If you want to cheat, activate this line
    print(f"I just chose a random number for you from {bottom_range} to {top_range}.")
    NUMBER_OF_ATTEMPTS[0] = number_of_attempts_desired



def advanced_mid_game():
    bottom_range = top_range = ''
    number_of_attempts_desired = input("1. Enter the number of attempts that you wish (1:∞): ")
    number_of_attempts_desired = int_made(number_of_attempts_desired)
    if not number_of_attempts_desired:
        print("Incorrect data.")
        advanced_mid_game()
    elif number_of_attempts_desired == 1:
        print("Hm... you're a cocky dude. You have only 1 attempt!")
    else:
        print(f"You'll have {number_of_attempts_desired} attempts.")
    bottom_range = input("2. Enter the |bottom| of random number range (1:∞): ")
    bottom_range = int_made(bottom_range)
    if not bottom_range:
        print("Incorrect data.")
        advanced_mid_game()
    top_range = input("3. Enter the |top| of random number range (*greater then previous number*): ")
    top_range = int_made(top_range)
    if not top_range or bottom_range > top_range:
        print("Incorrect data.")
        advanced_mid_game()
    print(bottom_range, top_range)
    SECRET_NUMBER[0] = random.randint(bottom_range, top_range)
    # print('SECRET>>>', SECRET_NUMBER[0], '<<<SECRET')                      # If you want to cheat, activate this line
    print(f"I just chose a random number for you from {bottom_range} to {top_range}.")
    NUMBER_OF_ATTEMPTS[0] = number_of_attempts_desired