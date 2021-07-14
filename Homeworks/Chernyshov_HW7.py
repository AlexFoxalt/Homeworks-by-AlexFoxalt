"""Алексей Чернышов HW7

Пишем игру. Программа выбирает из диапазона чисел (пусть для начала будет 1-100) случайное число и предлагает
пользователю его угадать. Пользователь вводит число. Если пользователь не угадал - предлагает пользователю угадать
еще раз, пока он не угадает. Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить. N -
Прекратить * Добавить в задание 2 счетчик попыток и диапазон чисел (начало и конец). Пользователь вводит количество
попыток, за которые он может угадать число, начало и конец диапазона. На каждом шаге угадывания числа сообщайте
пользователю сколько попыток у него осталось. Если пользователь не смог угадать за отведенное количество попыток
сообщить ему об окончании (Looser!). ** Добавить в задание 2 вывод сообщения-подсказки. Если пользователь ввел число,
и не угадал - сообщать: "Холодно" если разница между загаданным и введенным числами больше 10, "Тепло" - если от 5 до
10 и "Горячо" если от 4 до 1. """

import random
import sys


def int_made(x):
    """In our game we need items only with int type, so this function will replace all input data from str > int"""
    try:
        x = int(x)
    except ValueError:
        x = 0
    return x


def early_game():
    """Start of the game, Y = begin the game, N = end the game"""
    while True:
        ans = input("Start the game? (Y/N): ").upper()
        if ans == 'N':
            print("You left without starting...")
            sys.exit()
        elif ans == 'Y':
            print(">>> Let's get ready to rumble <<<")
            break
        else:
            print("!Error! Incorrect data.")


SECRET_NUMBER = [0]
NUMBER_OF_ATTEMPTS = [0]


def mid_game():
    """This function help to restart the game with new secret number"""
    SECRET_NUMBER[0] = random.randint(1, 100)
    # print('SECRET>>>', SECRET_NUMBER[0], '<<<SECRET')                      # If you want to cheat, activate this line
    print("I just chose a random number for you from 1 to 100.")


def advanced_mid_game():
    """Advanced mid_game function, here you can choose the number of attempts and enter the range of random numbers"""
    bot_and_top_range = [0, 0]
    number_of_attempts_desired = input("1. Enter the number of attempts that you wish (1:∞): ")
    number_of_attempts_desired = int_made(number_of_attempts_desired)
    if not number_of_attempts_desired:
        print("Incorrect data. (number of attempts)")
        advanced_mid_game()
    elif number_of_attempts_desired == 1:
        print("Hm... you're a cocky dude. You'll have only 1 attempt!")
    else:
        print(f"You'll have {number_of_attempts_desired} attempts.")
    bot_and_top_range[0] = input("2. Enter the |bottom| of random number range (1:∞): ")
    bot_and_top_range[1] = input("3. Enter the |top| of random number range (*greater then previous number*): ")
    bot_and_top_range[0] = int_made(bot_and_top_range[0])
    bot_and_top_range[1] = int_made(bot_and_top_range[1])
    if not bot_and_top_range[0] or not bot_and_top_range[1] or bot_and_top_range[0] >= bot_and_top_range[1]:
        print("Incorrect data. (top or bottom range or both)")
        advanced_mid_game()
    else:
        SECRET_NUMBER[0] = random.randint(bot_and_top_range[0], bot_and_top_range[1])
        print(f"I just chose a random number for you from {bot_and_top_range[0]} to {bot_and_top_range[1]}.")
    # print('SECRET>>>', SECRET_NUMBER[0], '<<<SECRET')                      # If you want to cheat, activate this line
    NUMBER_OF_ATTEMPTS[0] = number_of_attempts_desired


def end_game():
    """Main function, collecting data from gamer, and return a result"""
    while True:
        answer = input("Try to guess it: ")
        answer = int_made(answer)
        if not answer:
            print("!Error! Incorrect data.")
            end_game()
        print(f"Your number is '{answer}'")
        if answer == SECRET_NUMBER[0]:
            restart_answer = input(
                f"And my number is\n. . . .\n. . . .\n. . . .\n!{SECRET_NUMBER[0]}! \nWOOOOW!!!GREAT "
                f"JOB!!! Houdini, is it you? Nevermind... Let's do it one more time with another "
                f"random number?(Y/else=exit): ")
            if restart_answer.upper() == "Y":
                mid_game()
            else:
                print("Good bye, my little magician!......or cheater, who knows......")
                sys.exit()
        elif answer != SECRET_NUMBER[0]:
            restart_answer = input(
                "I'm sorry, but not this time... Do you want to have one more chance?(Y/else=exit): ")
            if restart_answer.upper() == 'Y':
                end_game()
            else:
                print("Did you give up so easily? Ok. Maybe next time.")
                sys.exit()


def advanced_end_game():
    """Advanced main function, attempts are limited."""
    while True:
        answer = input("Try to guess it: ")
        answer = int_made(answer)
        if not answer:
            print("!Error! Incorrect data.")
            advanced_end_game()
        print(f"Your number is '{answer}'")
        if answer == SECRET_NUMBER[0]:
            restart_answer = input(
                f"And my number is\n. . . .\n. . . .\n. . . .\n!{SECRET_NUMBER[0]}! \nWOOOOW!!!GREAT "
                f"JOB!!! Houdini, is it you? Nevermind... Let's do it one more time with another "
                f"random number?(Y/else=exit): ")
            if restart_answer.upper() == "Y":
                advanced_mid_game()
            else:
                print("Good bye, my little magician!......or cheater, who knows......")
                sys.exit()
        elif answer != SECRET_NUMBER[0]:
            NUMBER_OF_ATTEMPTS[0] -= 1
            if NUMBER_OF_ATTEMPTS[0] == 0:
                print(f"You lost! Good luck next time! My number was: {SECRET_NUMBER[0]}!")
                sys.exit()
            restart_answer = input(f"Attempts left: {NUMBER_OF_ATTEMPTS[0]}! I'm sorry, but not this time... Do you "
                                   f"want to have one more chance?(Y/else=exit): ")
            if restart_answer.upper() == 'Y':
                advanced_end_game()
            else:
                print("Did you give up so easily? Ok. Maybe next time.")
                sys.exit()


def advanced_end_game_with_help():
    """Advanced main function, attempts are limited, help tips added."""
    while True:
        answer = input("Try to guess it: ")
        answer = int_made(answer)
        if not answer:
            print("!Error! Incorrect data.")
            advanced_end_game_with_help()
        print(f"Your number is '{answer}'")
        if answer == SECRET_NUMBER[0]:
            restart_answer = input(
                f"And my number is\n. . . .\n. . . .\n. . . .\n!{SECRET_NUMBER[0]}! \nWOOOOW!!!GREAT "
                f"JOB!!! Houdini, is it you? Nevermind... Let's do it one more time with another "
                f"random number?(Y/else=exit): ")
            if restart_answer.upper() == "Y":
                advanced_mid_game()
            else:
                print("Good bye, my little magician!......or cheater, who knows......")
                sys.exit()
        elif answer != SECRET_NUMBER[0]:
            NUMBER_OF_ATTEMPTS[0] -= 1
            if NUMBER_OF_ATTEMPTS[0] == 0:
                print(f"You lost! Good luck next time! My number was: {SECRET_NUMBER[0]}!")
                sys.exit()
            help_tip_range = int(answer - SECRET_NUMBER[0])
            if help_tip_range in range(-4, 5):
                help_tip = "!HOT!(1:4)"
            elif help_tip_range in range(-5, 11):
                help_tip = "...Warm...(5:10)"
            else:
                help_tip = ".cold.(10+)"
            restart_answer = input(f"Attempts left: {NUMBER_OF_ATTEMPTS[0]}! I'm sorry, but not this time... Okay, "
                                   f"i'll help you...this time...you was: {help_tip}\nDo you want to have one more "
                                   f"chance?(Y/else=exit): ")
            if restart_answer.upper() == 'Y':
                advanced_end_game_with_help()
            else:
                print("Did you give up so easily? Ok. Maybe next time.")
                sys.exit()


""""-----------------------------------------------------------------------------------------------------------------"""


def game_diff_easy():
    """Easy mode: Endlessly trying, quit any time. """
    early_game()
    print('Difficult: Easy')
    mid_game()
    end_game()


def game_diff_middle():
    """Mid difficult: Attempts are limited, range of random number is chosen, help tips are available."""
    early_game()
    print("Difficult: Middle")
    print("Now you have to choose the number of attempts for which you think you will guess the number, \nas well as "
          'the range of numbers from which I will choose a random one.\n===MIDDLE DIFFICULT FEATURE===\nAfter every '
          "failed attempt, i'll help you a bit. If your guessed number will be in range:\na. *your number's range* "
          "10+ symbols --------------------> .cold.\nb. *your number's range* = from 5 to 10 symbols ---------> "
          "...Warm...\nc. *your number's range* = from 4 to 1 ------------------> !HOT!")
    advanced_mid_game()
    advanced_end_game_with_help()


def game_diff_hard():
    """Hard difficult: Attempts are limited, range of random number is chosen, help tips are NOT available."""
    early_game()
    print("Difficult: Hard")
    print("Now you have to choose the number of attempts for which you think you will guess my number, \nas well as "
          "the range of numbers from which I will choose a random one.")
    advanced_mid_game()
    advanced_end_game()


"""------------------------------------------------------------------------------------------------------------------"""


def start():
    """Game launcher"""
    res = input("Hello! My name is Bill Cipher and it's my game! First of all choose the difficult (easy, mid, "
                "hard): ").lower()
    if res == 'easy':
        return game_diff_easy()
    elif res == 'mid':
        return game_diff_middle()
    elif res == 'hard':
        return game_diff_hard()
    else:
        print('Incorrect data.')
        start()


# start()  # If you want to start the game- activate this line
