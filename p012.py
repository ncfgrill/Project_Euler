################################################################################
#                    P12: Highly divisible triangular number                   #
################################################################################
#                                                                              #
#           What is the value of the first triangular number to have           #
#                          over five hundred divisors?                         #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import ceil, sqrt

def find_factors(num):
    factors = []
    if num == 1: return [1]

    for f1 in range(1, ceil(sqrt(num)) + 1):
        if num % f1 == 0:
            f2 = num // f1
            factors.append(f1)
            factors.append(f2)

    return factors

def get_number():
    n_factors, num, inc = 0, 0, 1

    while n_factors <= 500:
        num += inc
        inc += 1
        n_factors = len(find_factors(num))

    return num

print('Triangle number:', get_number())
