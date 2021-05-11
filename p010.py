################################################################################
#                         P10: Summation of primes                             #
################################################################################
#                                                                              #
#             Find the sum of all the primes below two million.                #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import ceil, sqrt

def check_prime(num):
    if num <= 3:                        return num if num > 1 else 0
    elif num % 6 != 1 and num % 6 != 5: return 0

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0: return 0

    return num

print('Sum:', 2 + sum(list(map(check_prime, [i for i in range(3,2000000,2)]))))
