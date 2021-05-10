################################################################################
#                              P7: 10001st prime                               #
################################################################################
#                                                                              #
#                          What is the 10001st prime?                          #
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

def get_prime():
    i, p = 2, 1
    while i < 10002:
        p += 2
        if check_prime(p): i += 1

    return p

print('10001st prime:', get_prime())
