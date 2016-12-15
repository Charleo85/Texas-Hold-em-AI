import random
from matplotlib import pyplot as plt

class player(object):
    def __init__(self, num_card):
        if num_card < 3: self.error('Too few cards!')
        self.bets = [1] * num_card
        self.total = [2] * num_card
        self.probs = []
        for i in range(num_card): self.probs.append([])

    def error(self, error_message=''):
        print(error_message)
        exit(1)

    def analyze(self, card, first_dec, second_dec, res):
        pass

    def make_decision(self, card):
        if card < 0 or card >= len(self.bets):
            self.error('Incorrect card number')
        rd = random.random()
        return rd < (self.bets[card] / self.total[card])

    def get_prob(self, card):
        if card < 0 or card >= len(self.bets):
            self.error('Incorrect card number')
        return self.bets[card] / self.total[card]

    def is_good(self):
        for prob_array in self.probs:
            if len(prob_array) < precision: return False
        return True

    def get_prob_array(self, card):
        if card < 0 or card >= len(self.bets):
            self.error('Incorrect card number')
        return self.probs[card]

class first_player(player):
    def analyze(self, card, first_dec, second_dec, res):
        if card < 0 or card >= len(self.bets):
            self.error('Incorrect card number')
        # print(self.total[card])
        if len(self.probs[card]) >= precision: return

        self.probs[card].append( self.get_prob(card) )
        self.total[card] += 1

        if card == len(self.bets) - 1:
            self.bets[card] += 1
        elif first_dec and second_dec and res: # show down and win
            self.bets[card] += 1
        elif first_dec and not second_dec: # bluff success
            self.bets[card] += 1
        elif not first_dec and not res: # check and lose, should bet maybe
            self.bets[card] += 1 / len(self.bets)
        elif not first_dec and res: # check and win, should bet
            self.bets[card] += 1 - 1 / len(self.bets)


class second_player(player):
    def analyze(self, card, first_dec, second_dec, res):
        if card < 0 or card >= len(self.bets):
            self.error('Incorrect card number')
        if len(self.probs[card]) >= precision: return

        self.probs[card].append(self.get_prob(card))
        self.total[card] += 1

        if card == len(self.bets) - 1: # best card, should bet
            self.bets[card] += 1
        elif card == 0: # don't have any chance to win, should fold
            self.bets[card] += 0
        elif first_dec and second_dec and not res: # showdown and win
            self.bets[card] += 1
        elif first_dec and not second_dec: # fold, but should bet maybe
            self.bets[card] += 1 / (len(self.bets) - card)

def deal_cards(num_card):
    card1 = card2 = 0
    while card1 == card2:
        card1 = random.randint(0, num_card - 1)
        card2 = random.randint(0, num_card - 1)
    return card1, card2

def main():
    global precision
    precision = int(input('Enter the precision: '))
    num_card = int(input('Enter the number of cards: '))
    p1 = first_player(num_card)
    p2 = second_player(num_card)

    while (not p1.is_good()) or (not p2.is_good()):
        card1, card2 = deal_cards(num_card)
        first_dec = p1.make_decision(card1)
        second_dec = p2.make_decision(card2)
        res = (card1 > card2)
        p1.analyze(card1, first_dec, second_dec, res)
        p2.analyze(card2, first_dec, second_dec, res)

    to_show = int(input('Enter the player to plot: '))
    for i in range(num_card):
        if to_show == 1: plt.plot(p1.get_prob_array(i))
        elif to_show == 2: plt.plot(p2.get_prob_array(i))
    plt.show()

if __name__ == '__main__': main()
