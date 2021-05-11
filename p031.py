################################################################################
#                               P31: Coin sums                                 #
################################################################################
#                                                                              #
#       How many different ways can £2 be made using any number of coins?      #
#            Coins: 1p, 2p, 5p, 10p, 20p, 50p, 100p (£1), 200p (£2)            #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

coins = [200, 100, 50, 20, 10, 5, 2, 1]
combs = 0

def combinations(value, c):
    global combs
    if value != 0:
        if value < coins[c]: combinations(value, c+1)
        else:
            combinations(value - coins[c], c)
            if c + 1 < len(coins): combinations(value, c+1)
    
    else: combs += 1

combinations(200, 0)
print('Combinations:', combs)
