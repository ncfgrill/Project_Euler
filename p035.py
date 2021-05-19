################################################################################
#                              P35: Circular primes                            #
################################################################################
#                                                                              #
#             How many circular primes are there below one million?            #
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

def circle_num(num):
    return int(num[1:] + num[0])

def find_primes(p):
    if any(e in str(p) for e in '02468') or not check_prime(p): return 0

    save, c = p, circle_num(str(p))
    while c != save:
        if not check_prime(c): break
        c = circle_num(str(c))

    return 1 if c == save else 0

print('Primes:', 1 + sum(map(find_primes, [x for x in range(3,1000000,2)])))
