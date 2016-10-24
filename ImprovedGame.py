import random

def first_decision(hand):
    if hand == 0 or hand == 1: # Q, K plays randomly
        random_num = random.random()
        if random_num <= 0.25:
            return 0
        elif random_num <= 0.5:
            return 1
        elif random_num <= 0.75:
            return 2
        else:
            return 3
    else: # A always bets maximum size
        return 3

def second_decision(hand):
    if hand == 0: # Q always fold
        return 0
    elif hand == 1: # K plays randomly
        random_num = random.random()
        if random_num <= 0.5:
            return 0
        else:
            return 1
    else: # A always calls
        return 1

def play_game(hand1, hand2):
    invested = 1
    bet = first_decision(hand1)
    if bet == 0:
        return (0, -invested)

    invested += bet
    call_or_fold = second_decision(hand2)
    if call_or_fold == 0:
        return (bet, 1)

    if hand1 > hand2:
        return (bet, invested)
    else:
        return (bet, -invested)

# h1=hand1, h2=hand2, bs=bet_size, e=earning
print('h1 h2 bs e')

# play game for 1000 times and test for results
for i in range(1000):
    # deal cards
    hand1 = hand2 = 0
    while (hand1 == hand2):
        hand1 = random.randint(0, 2)
        hand2 = random.randint(0, 2)

    (bet, earning) = play_game(hand1, hand2)
    print(hand1, hand2, bet, earning)
