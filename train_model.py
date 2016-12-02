import random
from matplotlib import pyplot as plt

OPT_K_BET = 1/2
OPT_Q_BET = 1/3
OPT_K_CALL = 1/4

def training_player_first(card, k_call):
    if card == 0:
        return k_call <= OPT_K_CALL
    elif card == 1:
        rd = random.random()
        return rd > 0.5
    else:
        return True

def training_player_second(card, q_bet):
    if card == 0:
        return False
    elif card == 1:
        return q_bet >= OPT_Q_BET
    else:
        return True

def deal_cards(is_first, card):
    card1 = card2 = 0
    while card1 == card2:
        if is_first:
            card1 = card
            card2 = random.randint(0, 2)
        else:
            card1 = random.randint(0, 2)
            card2 = card
    return (card1, card2)

def get_game_data(is_first, card, precision):
    data = []
    showdown = 1
    total = 2
    while total < precision + 2:
        prob = showdown / total
        card1, card2 = deal_cards(is_first, card)
        if is_first:
            if not training_player_second(card2, prob):
                showdown += 1
            else:
                if card1 > card2: showdown += 1
            total += 1
            data.append(prob)
        elif training_player_first(card1, prob):
            if card1 < card2: showdown += 1
            total += 1
            data.append(prob)
    return data

def get_precision():
    precision = 0
    while precision == 0:
        try:
            msg = 'Please enter the precision'
            precision = int(input(msg + ': '))
        except ValueError:
            precision = 0
    return precision

def get_decision():
    decision = 0
    while decision != 1 and decision != 2:
        try:
            msg = 'Select: 1) 1st player, 2) 2nd player'
            decision = int(input(msg + ': '))
        except ValueError:
            decision = 0
    return decision == 1

def main():
    precision = get_precision()
    decision = get_decision()
    plt.plot(get_game_data(decision, 0, precision))
    plt.plot(get_game_data(decision, 1, precision))
    plt.plot(get_game_data(decision, 2, precision))
    if decision:
        plt.text(0.8*precision, 0.35, r'$P(Q)=\frac{1}{3}$')
        plt.text(0.8*precision, 0.55, r'$P(K)=\frac{1}{2}$')
        plt.text(0.8*precision, 0.95, r'$P(A)=1$')
    else:
        plt.text(0.8*precision, 0.05, r'$P(Q)=0$')
        plt.text(0.8*precision, 0.30, r'$P(K)=\frac{1}{4}$')
        plt.text(0.8*precision, 0.95, r'$P(A)=1$')
    plt.show()

if __name__ == '__main__':
    main()
