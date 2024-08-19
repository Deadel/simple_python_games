import random
from art import logo
'''FUNCKJE'''

def dif_level():
    choose = input("Choose your level of difficulty:\n1. easy life=15\n2. medium life=10\n3. hard life=5\n")
    if choose =='1':
        print("youi choose easy level")
        return 15
    elif choose == '2':
        print("youi choose medium level")
        return 10
    else:
        print("youi choose hard level")
        return 5

# def check(player_guess, guess_numer, life):
#     if player_guess == guess_numer:
#         print(f"You are right! This is {guess_numer}")
#         carry_on = False
#     elif player_guess > guess_numer:
#         print("My number is lower.")
#         life -= 1
#         print(f"You have {life} life")
#     elif player_guess < guess_numer:
#         print("My number is higher.")
#         life -= 1
#         print(f"You have {life} life")
#
#     if life == 0:
#         print("you lose!")
#         carry_on = False

def game():
    print(logo)
    game_on = True
    while game_on:
        guess_numer = random.randint(1,100)
        print("I think about number between 1 and 100.\nCan you guess what is this number? ")
        life = dif_level()
        print(f"You have {life} life")
        carry_on = True

        while carry_on:
            try:
                player_guess = int(input("So what number i choose? "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if player_guess == guess_numer:
                print(f"You are right! This is {guess_numer}")
                carry_on = False
            elif player_guess > guess_numer:
                print("My number is lower.")
                life -= 1
                print(f"You have {life} life")
            elif player_guess < guess_numer:
                print("My number is higher.")
                life -= 1
                print(f"You have {life} life")

            if life == 0:
                print("you lose!")
                carry_on = False

        next_game = input("Do you wanna play again?\n1.'yes'\n2.'no'")
        if next_game in ['1', 'y', 'yes', 'Y']:
            pass
        elif next_game in ['2', 'n', 'no', 'N']:
            game_on = False

game()