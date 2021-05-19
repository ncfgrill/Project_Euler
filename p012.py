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
    factors = {1, num}

    for f1 in range(2, ceil(sqrt(num)) + 1):
        if num % f1 == 0:
            f2 = num // f1
            factors.add(f1)
            factors.add(f2)

    return len(factors)

def get_number():
    n_factors, num, inc = 0, 0, 1

    while n_factors <= 500:
        num += inc
        inc += 1
        n_factors = find_factors(num)

    return num

print('Triangle number:', get_number())
