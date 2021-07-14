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

SECRET_NUMBER = [0]
NUMBER_OF_ATTEMPTS = [0]
CHOSEN_DIFFICULTY = [""]
EXIT_CODE = [1]


def int_made(x):
    """In our game we need items only with int type, so this function will replace all input data from str > int"""
    try:
        x = int(x)
    except ValueError:
        x = 0
    return x


def early_game():
    """Start of the game, Y = begin the game, N = end the game"""
    ans = [""]
    ans[0] = input("Start the game? (Y/N): ").upper()
    if ans[0] == 'N':
        print("You left without starting...")
        EXIT_CODE[0] = 0
        start()
    elif ans[0] == 'Y':
        print(">>> Let's get ready to rumble <<<")
        if CHOSEN_DIFFICULTY[0] == 'Easy':
            mid_game()
        else:
            advanced_mid_game()
    else:
        print("\033[1;30;41mIncorrect data.\033[1;m")
        early_game()


def mid_game():
    """This function help to restart the game with new secret number"""
    print(f"Difficult: {CHOSEN_DIFFICULTY[0]}")
    SECRET_NUMBER[0] = random.randint(1, 100)
    # print('SECRET>>>', SECRET_NUMBER[0], '<<<SECRET')                      # If you want to cheat, activate this line
    print("I just chose a random number for you from 1 to 100.")
    end_game()


def advanced_mid_game():
    """Advanced mid_game() function. Now gamer can choose the number of attempts and the range of random numbers,
    if you chose hard mode - the game won't have restart option """
    print(f"Difficult: {CHOSEN_DIFFICULTY[0]}")
    print("Now you have to choose the number of attempts for which you think you will guess the number, \nas well as "
          "the range of numbers from which I will choose a random one.")
    bot_and_top_range = [0, 0]
    number_of_attempts_desired = input("1. Enter the number of attempts that you wish (1:∞): ")
    number_of_attempts_desired = int_made(number_of_attempts_desired)
    if not number_of_attempts_desired:
        print("\033[1;30;41mIncorrect data.\033[1;m (number of attempts)")
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
        print("\033[1;30;41mIncorrect data.\033[1;m (top or bottom range or both)")
        advanced_mid_game()
    else:
        SECRET_NUMBER[0] = random.randint(bot_and_top_range[0], bot_and_top_range[1])
        print(f"I just chose a random number for you from {bot_and_top_range[0]} to {bot_and_top_range[1]}.")
    # print('SECRET>>>', SECRET_NUMBER[0], '<<<SECRET')                      # If you want to cheat, activate this line
    NUMBER_OF_ATTEMPTS[0] = number_of_attempts_desired
    if CHOSEN_DIFFICULTY[0] == 'Middle':
        advanced_end_game_with_help()
    elif CHOSEN_DIFFICULTY[0] == 'Hard':
        advanced_end_game()


def end_game():
    """End function, collecting data from gamer, and return a result"""
    answer = input("Try to guess it: ")
    answer = int_made(answer)
    if not answer:
        print("\033[1;30;41mIncorrect data.\033[1;m")
        end_game()
    print(f"Your number is \033[1;1;32m{answer}\033[1;m")
    if answer == SECRET_NUMBER[0]:
        restart_answer = input(
            f"And my number is\n. . . .\n. . . .\n. . . .\n!\033[1;30;46m{SECRET_NUMBER[0]}\033[1;m! \nWOOOOW!!!GREAT "
            f"JOB!!! Houdini, is it you? Nevermind... Let's do it one more time with another "
            f"random number?(Y/else=exit): ")
        if restart_answer.upper() == "Y":
            mid_game()
        else:
            print("Good bye, my little magician!......or cheater, who knows......")
            EXIT_CODE[0] = 0
            start()
    elif answer != SECRET_NUMBER[0]:
        restart_answer = input(
            "I'm sorry, but not this time... Do you want to have one more chance?(Y/else=exit): ")
        if restart_answer.upper() == 'Y':
            end_game()
        else:
            print(f"Did you give up so easily? Ok. Maybe next time. "
                  f"My number was: \033[1;1;35m{SECRET_NUMBER[0]}\033[1;m!")
            EXIT_CODE[0] = 0
            start()


def advanced_end_game():
    """Advanced end function, attempts are limited, you CAN'T restart a game with new random number."""
    answer = input("Try to guess it: ")
    answer = int_made(answer)
    if not answer:
        print("\033[1;30;41mIncorrect data.\033[1;m")
        advanced_end_game()
    print(f"Your number is \033[1;1;32m{answer}\033[1;m")
    if answer == SECRET_NUMBER[0]:
        restart_answer = input(
            f"And my number is\n. . . .\n. . . .\n. . . .\n!{SECRET_NUMBER[0]}! \nWOOOOW!!!GREAT "
            f"JOB!!! Houdini, is it you? Nevermind... Let's do it one more time with another "
            f"random number?(Y/else=exit): ")
        if restart_answer.upper() == "Y":
            advanced_mid_game()
        else:
            print("Good bye, my little magician!......or cheater, who knows......")
            EXIT_CODE[0] = 0
            start()
    elif answer != SECRET_NUMBER[0]:
        NUMBER_OF_ATTEMPTS[0] -= 1
        if NUMBER_OF_ATTEMPTS[0] == 0:
            print(f"You lost! You have no more extra chances! My number was: \033[1;1;35m{SECRET_NUMBER[0]}\033[1;m!")
            sys.exit()
        restart_answer = input(f"Attempts left: [4;1;31m{NUMBER_OF_ATTEMPTS[0]}\033[1;m'! I'm sorry, but not this "
                               f"time... Do you want to have one more chance?(Y/else=exit): ")
        if restart_answer.upper() == 'Y':
            advanced_end_game()
        else:
            print(f"Did you give up so easily? Ok. Maybe next time."
                  f"My number was: \033[1;1;35m{SECRET_NUMBER[0]}\033[1;m!")
            EXIT_CODE[0] = 0
            start()


def advanced_end_game_with_help():
    """Helps not to see this text, if gamer retry to guess the number"""
    print("===MIDDLE DIFFICULT FEATURE===\nAfter every failed attempt, i'll help you a bit. If your guessed number "
          "will be in range:\na. *your number's range* 10+ symbols --------------------> \033[1;1;29m.cold.\033[1;m"
          "\nb. *your number's range* = from 5 to 10 symbols ---------> \033[1;1;33m...Warm...\033[1;m\nc. *your "
          "number's range* = from 4 to 1 ------------------> \033[1;1;31m!HOT!\033[1;m")
    advanced_end_game_with_help_lvl2()


def advanced_end_game_with_help_lvl2():
    """Advanced end function, attempts are limited, help tips added, you can restart a game with new random number."""
    answer = input("Try to guess it: ")
    answer = int_made(answer)
    if not answer:
        print("\033[1;30;41mIncorrect data.\033[1;m")
        advanced_end_game_with_help_lvl2()
    print(f"Your number is \033[1;1;32m{answer}\033[1;m")
    if answer == SECRET_NUMBER[0]:
        restart_answer = input(
            f"And my number is\n. . . .\n. . . .\n. . . .\n!{SECRET_NUMBER[0]}! \nWOOOOW!!!GREAT "
            f"JOB!!! Houdini, is it you? Nevermind... Let's do it one more time with another "
            f"random number?(Y/else=exit): ")
        if restart_answer.upper() == "Y":
            advanced_mid_game()
        else:
            print("Good bye, my little magician!......or cheater, who knows......")
            EXIT_CODE[0] = 0
            start()
    elif answer != SECRET_NUMBER[0]:
        NUMBER_OF_ATTEMPTS[0] -= 1
        if NUMBER_OF_ATTEMPTS[0] == 0:
            print(f"You lost! Good luck next time! My number was: \033[1;1;35m{SECRET_NUMBER[0]}\033[1;m!")
            restart_answer = input("Let's do it one more time with another random number?(Y/else=exit): ")
            if restart_answer.upper() == 'Y':
                advanced_mid_game()
            else:
                print(f"Today i defeated you! My number was: \033[1;1;35m{SECRET_NUMBER[0]}\033[1;m!")
                EXIT_CODE[0] = 0
                start()
        help_tip_range = int(answer - SECRET_NUMBER[0])
        if help_tip_range in range(-4, 5):
            help_tip = "\033[1;1;31m!HOT!\033[1;m (1:4)"
        elif help_tip_range in range(-5, 11):
            help_tip = "\033[1;1;33m...Warm...\033[1;m (5:10)"
        else:
            help_tip = "\033[1;1;29m.cold.\033[1;m (10+)"
        restart_answer = input(f"Attempts left: '\033[4;1;31m{NUMBER_OF_ATTEMPTS[0]}\033[1;m'! I'm sorry, but not "
                               f"this time... Okay, i'll help you...this time...you was: {help_tip}\nDo you want to "
                               f"have one more chance?(Y/else=exit): ")
        if restart_answer.upper() == 'Y':
            advanced_end_game_with_help_lvl2()
        else:
            print(f"Did you give up so easily? Ok. Maybe next time."
                  f"My number was: \033[1;1;35m{SECRET_NUMBER[0]}\033[1;m!")
            EXIT_CODE[0] = 0
            start()


"""------------------------------------------------------------------------------------------------------------------"""


def start():
    """Game launcher"""
    while EXIT_CODE[0] == 1:
        res = input("Hello! My name is \033[1;1;34mBill\033[1;m \033[1;1;35mCipher\033[2;m and it's my game! First of "
                    "all choose the difficult (easy, mid, hard): ").lower()
        if res == "easy":
            CHOSEN_DIFFICULTY[0] = "Easy"
            print("\033[1;1;32mEasy mode:\033[1;m An infinite number of attempts, you can exit at any time, "
                  "you can re-select a random number.")
            return early_game()
        elif res == "mid":
            CHOSEN_DIFFICULTY[0] = "Middle"
            print("\033[1;1;33mMiddle mode:\033[1;m You can choose the number of attempts, a range of random numbers, "
                  "after each failure a hint will pop up, the possibility to choose a new random number after defeat.")
            return early_game()
        elif res == "hard":
            CHOSEN_DIFFICULTY[0] = "Hard"
            print("\033[1;1;31mHard mode:\033[1;m You can choose the number of attempts, the range of random numbers, "
                  "there are NO hints, there is NO possibility to choose a new random number after defeat.")
            return early_game()
        else:
            print("\033[1;30;41mIncorrect data.\033[1;m")
            start()


# start()                                                            # If you want to start the game- activate this line
start()
