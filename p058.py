################################################################################
#                              P58: Spiral primes                              #
################################################################################
#                                                                              #
#  Starting with 1 and spiralling anticlockwise in the following way, a square #
#                     spiral with side length 7 is formed.                     #
#                                                                              #
#    If one complete new layer is wrapped around the spiral above, a square    #
# spiral with side length 9 will be formed. If this process is continued, what #
#  is the side length of the square spiral for which the ratio of primes along #
#                     both diagonals first falls below 10%?                    #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

from math import ceil, sqrt

def check_prime(num):
    if num <= 3:                        return num > 1
    elif num % 6 != 1 and num % 6 != 5: return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0: return False

    return True

def find_ratio():
    diag, primes, d = 1, 0, 1

    while True:
        d += 2
        d2 = d ** 2
        diag += 4
        for i in range(1, 4):
            if check_prime(d2 - (i * (d - 1))): primes += 1

        if primes / diag < 0.1: return d

print('Side length:', find_ratio())
