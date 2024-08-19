import random
from art import logo, vs
from game_data import data


def th_vs_game(choose_a, choose_b):
    follow_a = choose_a['follower_count']
    follow_b = choose_b['follower_count']
    print(f"Compere A: {choose_a['name']}, {choose_a['description']}, {choose_a['country']}.")
    print(vs)
    print(f"Against B: {choose_b['name']}, {choose_b['description']}, {choose_b['country']}.")
    bet = input("who have more followers?  'A' or 'B'\n").upper()
    if bet == 'A' and choose_a['follower_count'] > choose_b['follower_count']:
        return choose_a
    elif bet == 'B' and choose_a['follower_count'] < choose_b['follower_count']:
        return choose_b
    else:
        return 0


streak = 0
play_a_game = True


print(logo)
choose_a = random.choice(data)
while play_a_game:
    choose_b = random.choice(data)
    while choose_a == choose_b:
        choose_b = random.choice(data)
    result = th_vs_game(choose_a, choose_b)
    if result == 0:
        continue_play = input(f"Do you wanna play Again? Your score was {streak} \n1. 'yes'\n2. 'no").lower()
        streak = 0
        if continue_play in ['no', '2', 'n']:
            play_a_game = False
        else:
            choose_a = random.choice(data)
    else:
        streak += 1
        print(f"You are right! Your current score is: {streak}")
        choose_a = result

