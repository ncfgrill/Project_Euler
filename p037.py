################################################################################
#                            P37: Truncatable primes                           #
################################################################################
#                                                                              #
#  Find the sum of the only eleven primes that are both truncatable from left  #
#                          to right and right to left.                         #
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

def truncate(num):
    save = num
  
    #left-to-right
    while len(num) > 1:
        num = num[1:]
        if not check_prime(int(num)): return False

    num = save

    # right-to-left
    while len(num) > 1:
        num = num[0:-1]
        if not check_prime(int(num)): return False

    return True

def find_primes():
    primes, d, s = 0, 11, 0
    while primes < 11:
        if check_prime(d):
            if truncate(str(d)):
                primes += 1
                s += d

        d += 2

    return s

print('Sum:', find_primes())
