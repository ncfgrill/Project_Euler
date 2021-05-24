################################################################################
#                          P50: Consecutive prime sum                          #
################################################################################
#                                                                              #
#     Which prime, below one-million, can be written as the sum of the most    #
#                             consecutive primes?                              #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import ceil, sqrt

def check_prime(num):
    if num <= 3:                        return num > 1
    elif num % 6 != 1 and num % 6 != 5: return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0: return False

    return True

def find_prime():
    primes = [x for x in range(3, 4001, 2) if check_prime(x)]
    primes.insert(0, 2)

    prime = (0, 0)

    for i in range(len(primes) - 2):
        p, j = primes[i], i+1
        while j < len(primes) - 1:
            if i == 0 and j == 1:
                p += primes[j]
                j += 1
            else:
                p += primes[j] + primes[j+1]
                j += 2

            if p < 1000: continue
            elif p >= 1000000: break

            if check_prime(p) and j - i > prime[1]: prime = (p, j - i)

    return prime[0]

print('Prime:', find_prime())
