import random
from matplotlib import pyplot as plt

def get_precision():
    precision = 0
    while precision == 0:
        try:
            msg = 'Please enter the precision'
            precision = int(input(msg + ': '))
        except ValueError:
            precision = 0
    return precision

def get_self_data(precision):
    q_bet = k_call = est_q = est_k = 1
    data_q = []
    data_k = []
    while len(data_q) < precision or len(data_k) < precision:
        card1 = 0
        card2 = random.randint(1, 2)
        prob_q = q_bet / (len(data_q)+2)
        prob_k = k_call / (len(data_k)+2)
        pe_q = est_q / (len(data_q)+2)
        pe_k = est_k / (len(data_k)+2)

        if prob_k < pe_k: # this is q bet
            if card2 == 1 and prob_q > pe_q: # this is K call
                k_call += 1
                est_q += 1
                est_k += 1
                data_k.append(prob_k)
            elif card2 == 2: # this is meeting an Ace
                data_k.append(prob_k)
            else: # this is K fold
                est_q += 0.5
                q_bet += 1
        else: # this is q fold
            if card2 == 1:
                est_k += 0.5
                data_k.append(prob_k)
        data_q.append(prob_q)

    if len(data_q) >= precision: data_q = data_q[:precision]
    if len(data_k) >= precision: data_k = data_k[:precision]
    # return {'Q':data_q, 'K':data_k}
    plt.plot(data_q)
    plt.plot(data_k)
    plt.text(0.8*precision, 0.35, r'Q bluff')
    plt.text(0.8*precision, 0.27, r'K call')
    plt.show()

def main():
    precision = get_precision()
    get_self_data(precision)

if __name__ == '__main__':
    main()
