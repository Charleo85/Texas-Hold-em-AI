import random
import math

"""
According to our calculation:
the probaility that Q bets as first player should be sqrt(6)/2 - 1
and the probability that K bets as first player should be 1
"""
OPTIMAL_Q_BET = 0.5 * math.sqrt(6) - 1
OPTIMAL_K_BET = 1

"""
The function decision takes in two parameters:
1. isFirst: True if the bot is the first player, False otherwise;
2. hand: 0 if hand is Queen, 1 if hand is King, 2 if hand is Ace,
and returns True if the bot plays aggressively,
(bets if first player, or calls if second player)
or False if otherwise.
"""
def decision(isFirst, hand, prob_q_bet, prob_k_bet):
    randomNum = random.random()
    if (isFirst):  # bot plays the first position
        if (hand == 0):
            return randomNum <= prob_q_bet
        elif (hand == 1):
            return randomNum <= prob_k_bet
        else:
            return True  # Ace always bets in first position
    else:  # bot plays the second position
        if (hand == 0):
            return False  # Queen always folds to a bet
        elif (hand == 1):
            prob_k_call = prob_q_bet / (1 + prob_q_bet)
            return randomNum <= prob_k_call
        else:
            return True  # Aces always calls a bet

def testDecision(n):  # Tests the bluff decision of Queen n times
    count = 0
    for i in range(n):
        if (decision(True, 0, OPTIMAL_Q_BET, OPTIMAL_K_BET)):
            count += 1
    print(str(count) + " out of " + str(n) + " times of bluffing.")

# testDecision(1000)  # Test for 1000 times
