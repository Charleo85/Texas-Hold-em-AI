import random
import matplotlib.pyplot as plt

from PokerBot import *

# returns an int that represents the earning of a model in a single game
# Note: model plays first here
def game_model_first(model_card, model_decision, bot_card, prob_q_bet):
    if model_decision: # model bets
        bot_decision = decision(False, bot_card, prob_q_bet, OPTIMAL_K_BET)
        if bot_decision:
            if model_card < bot_card:
                return -2
            else:
                return 2
        else:
            return 1
    else: # model folds
        return -1

# the total earning of a Q player if he makes $num_bets out of $precision bets
def queen_earning(num_bets, precision):
    total_earning = 0
    for i in range(precision):
        model_decision = i < num_bets
        bot_card = random.randint(1, 2)
        prob_q_bet = num_bets / precision
        total_earning += game_model_first(0, model_decision, bot_card, prob_q_bet)
    return total_earning

# based on the given precision, tests every number of bets that Q could make
def queen_graph(precision):
    x = []
    y = []
    for i in range(0, precision+1, 1):
        x.append(i)
        y.append(queen_earning(i, precision))
    plt.plot(x, y, 'g^')
    plt.show()

queen_graph(1000)
