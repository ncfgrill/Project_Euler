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
    if '0' in str(p) or '2' in str(p) or\
       '4' in str(p) or '6' in str(p) or '8' in str(p):
        return 0
    if not check_prime(p): return 0

    save = p
    c = save
    while True:
        c = circle_num(str(c))
        if c == save or not check_prime(c): break

    return 1 if c == save else 0

print('Primes:', 1 + sum(map(find_primes, [x for x in range(3, 1000000, 2)])))
