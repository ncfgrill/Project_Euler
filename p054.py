################################################################################
#                               P54: Poker hands                               #
################################################################################
#                                                                              #
#  Given the input of one-thousand competing poker hands, how many hands does  #
#                                Player 1 win?                                 #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

def rank_hand(values, suits):
    # Arbitrary values to give order to hand rank
    hand_values = {'HC':1, 'OP':2, 'TP':3, 'TK':4, 'ST':5,
                   'FL':6, 'FH':7, 'FK':8, 'SF':9, 'RF':10}

    num_values = len(values)
    num_suits = len(suits)

    hand_value = None   # Value of hand
    hand_value_best = 0 # Best card given hand type
    high_card = -1      # Only relevant for HC, OP, TP, FL

    # Returns 3-tuple (hand_value, hand_value best card, high card)
    if num_values == 2: # FH, FK
        for v in values:
            if values[v] == 3: # FH
                hand_value = hand_values['FH']
                hand_value_best = v
                break
            elif values[v] == 4: # FK
                hand_value = hand_values['FK']
                hand_value_best = v
                break
    elif num_values == 3: # TP, TK
        for v in values:
            if values[v] == 2: # TP
                if v > hand_value_best: # Find highest ranking pair
                    hand_value = hand_values['TP']
                    hand_value_best = v
            elif values[v] == 3: # TK
                hand_value = hand_values['TK']
                hand_value_best = v
                high_card = -1
                break
            else: # values[v] == 1
                if v > high_card: high_card = v # TP only
    elif num_values == 4: # OP
        for v in values:
            if values[v] == 1:
                if v > high_card: high_card = v
            else: # values[v] == 2
                hand_value = hand_values['OP']
                hand_value_best = v
    else: # HC, ST, FL SF, RF
        if max(values.keys()) - min(values.keys()) == 4: # ST, SF, RF
            if num_suits != 1: hand_value = hand_values['ST'] # ST
            else: # SF, RF
                if 14 in values: hand_value = hand_values['RF'] # RF
                else:            hand_value = hand_values['SF'] # SF
        else:
            if num_suits == 1: hand_value = hand_values['FL'] # FL
            else:              hand_value = hand_values['HC'] # HC
            hand_value_best = max(values.keys())

    return (hand_value, hand_value_best, high_card)

def compare_hands(h1, h2):
    hv1, hvb1, hc1 = h1[0], h1[1], h1[2]
    hv2, hvb2, hc2 = h2[0], h2[1], h2[2]

    if hv1 - hv2:     return max(hv1 - hv2, 0)
    elif hvb1 - hvb2: return max(hvb1 - hvb2, 0)
    else:             return max(hc1 - hc2, 0)

def better_hand(h1, h2):
    high_cards = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    h1_values, h1_suits, h2_values, h2_suits = {}, {}, {}, {}

    for i in range(len(h1)):
        h1_v, h1_s = h1[i][0], h1[i][1]
        h2_v, h2_s = h2[i][0], h2[i][1]

        try: h1_v = int(h1_v)
        except: h1_v = high_cards[h1_v]

        try: h2_v = int(h2_v)
        except: h2_v = high_cards[h2_v]

        if h1_v in h1_values: h1_values[h1_v] = h1_values[h1_v] + 1
        else:                 h1_values[h1_v] = 1

        if h2_v in h2_values: h2_values[h2_v] = h2_values[h2_v] + 1
        else:                 h2_values[h2_v] = 1

        if h1_s in h1_suits: h1_suits[h1_s] = h1_suits[h1_s] + 1
        else:                h1_suits[h1_s] = 1

        if h2_s in h2_suits: h2_suits[h2_s] = h2_suits[h2_s] + 1
        else:                h2_suits[h2_s] = 1

    return compare_hands(rank_hand(h1_values, h1_suits),
                         rank_hand(h2_values, h2_suits))

def find_winner(hands):
    return better_hand(hands[:5], hands[5:])

with open('p054_poker.txt') as f:
    p1 = 0
    for l in f.readlines():
        if find_winner(l.split(' ')): p1 += 1

    print('P1 wins:', p1)
