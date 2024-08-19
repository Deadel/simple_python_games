from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

print(logo)


def deal_card():
    card = random.choice(cards)
    return card


def calculate_score():

    player = sum(user_cards)
    computer = sum(computer_cards)

    print(f"Yours score is {player} amd cards {user_cards}")
    # print(computer_cards)
    # print(user_cards)

    if player == 21:
        player = 0
    elif computer == 21:
        computer = 0

    if player > 21:
        if 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
    elif computer > 21:
        if 11 in computer_cards:
            computer_cards.remove(11)
            computer_cards.append(1)

    if player == 0 and len(user_cards) == 2:
        print("you win!")
        return True
    elif computer == 0 and len(computer_cards) == 2 or player > 21:
        print("you lose!")
        return True
    else:
        return False

def compare():
    player = sum(user_cards)
    computer = sum(computer_cards)
    calculate_score()
    if player == computer:
        print(f'Your score is {player} and computer score is {computer}')
        print("it's draw!")
    elif player == 0:
        print(f'Your score is {player} and computer score is {computer}')
        print("you win!")
    elif computer == 0 or player > 21:
        print(f'Your score is {player} and computer score is {computer}')
        print("you lose!")
    elif computer > 21:
        print(f'Your score is {player} and computer score is {computer}')
        print("you win!")
    elif player > computer:
        print(f'Your score is {player} and computer score is {computer}')
        print("you win!")
    else:
        print(f'Your score is {player} and computer score is {computer}')
        print("you lose!")
    return True

def game():
    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    end = calculate_score()
    # print(end)
    while not end:
        print(f"Computer first card is {computer_cards[0]}")
        draw_next_card = input("Do you wanna draw next card?\n1.'yes'\n2.'no'")
        if draw_next_card in ['yes', '1', 'YES', 'Yes', 'y']:
            user_cards.append(deal_card())
            computer = sum(computer_cards)
            if computer < 17 and computer !=0:
                computer_cards.append(deal_card())
            end = calculate_score()
        else:
            end = compare()

game_on = 1
while game_on == 1:
    game()
    play_again = input("You want to restart the game?\n1.'yes'\n2.'no'")
    if play_again in ['yes', '1', 'YES', 'Yes', 'y']:
        print(logo)
        user_cards = []
        computer_cards = []
    else:
        game_on = 0
