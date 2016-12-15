import random
from matplotlib import pyplot as plt

# 4 Players: J Q K A
#       Bet:       1
#     Check:       1
#      Call: 0     1

def get_precision():
    while precision == 0:
        try:
            msg = 'Please enter the precision'
            precision = int(input(msg + ': '))
        except ValueError:
            precision = 0
    return precision

def get_self_data(precision):
    j_bet = q_bet = q_call = k_call = 1
    est_j_bet = est_q_bet = est_q_bet = est_k = 1
    data_j_bet = []
    data_q_bet = []
    data_q_call = []
    data_k_call = []
    while  min(len(data_j_bet), len(data_q_bet), len(data_q_call), len(data_k_call)) < precision : #iterate until preicison is reached
        card1 = random.randint(0, 1) # First card j or q
        if (card1 == 0):
            card2 = random.randint(1, 2, 3) # Second card q or k
        else:
            card2 = random.randint(2, 3) # Second card q or k

        prob_j_bet = j_bet / (len(data_j_bet)+2)
        prob_q_bet = q_bet / (len(data_q_bet)+2)
        prob_q_call = q_call / (len(data_q_call)+2)
        prob_k_call = k_call / (len(data_k_call)+2)

        pe_j_bet = est_j_bet / (len(data_j_bet)+2)
        pe_q_bet = est_q_bet / (len(data_q_bet)+2)
        pe_q_call = est_q_call / (len(data_q_call)+2)
        pe_k_call = est_k_call / (len(data_k_call)+2)

        if (card1 == 0): #first car is j
            if prob_k_call < pe_k_call: # k calling
                if card2 == 1 and prob_j_bet > pe_j_bet:
                    k_call += 1
                    est_j_bet += 1
                    est_k_call += 1
                    data_k.append(prob_k_call)
                elif card2 == 3: # this is meeting an Ace
                    data_k.append(prob_k_call)
                else: # this is K fold
                    est_j_bet += 0.5
                    j_bet += 1
            else: # this is j bluff success
                if card2 == 1:
                    est_k += 0.5
                    data_k.append(prob_k)
            data_j.append(prob_j)
        else:
            if prob_k < pe_k_call: # k calling
                if card2 == 1 and prob_j_bet > pe_j_bet:
                    k_call += 1
                    est_j_bet += 1
                    est_k_call += 1
                    data_k.append(prob_k_call)
                elif card2 == 3: # this is meeting an Ace
                    data_k.append(prob_k_call)
                else: # this is K fold
                    est_j_bet += 0.5
                    j_bet += 1
            else: # this is j bluff success
                if card2 == 1:
                    est_k += 0.5
                    data_k.append(prob_k)
            data_j.append(prob_j)

    if len(data_j_bet) >= precision: data_j_bet = data_j_bet[:precision]
    if len(data_q_bet) >= precision: data_q_bet = data_q_bet[:precision]
    if len(data_q_call) >= precision: data_q_call = data_q_call[:precision]
    if len(data_k_call) >= precision: data_k_call = data_k_call[:precision]
    # return {'J':data_j, 'K':data_k}

    plt.plot(data_j_bet)
    plt.plot(data_q_bet)
    plt.plot(data_q_call)
    plt.plot(data_k_call)
    plt.text(0.8*precision, 0.35, r'J bluff')
    plt.text(0.8*precision, 0.35, r'Q bluff')
    plt.text(0.8*precision, 0.35, r'Q call'
    plt.text(0.8*precision, 0.27, r'K call')
    plt.show()
