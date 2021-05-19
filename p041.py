################################################################################
#                            P41: Pandigital prime                             #
################################################################################
#                                                                              #
#           What is the largest n-digit pandigital prime that exists?          #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import ceil, sqrt

perm, right = [], 0

def check_prime(num):
    if num % 6 != 1 and num % 6 != 5: return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0: return False

    return True

def get_perm():
    global right, perm
    
    r1 = right
    while perm[r1] >= perm[r1+1]: r1 -= 1

    r2, lo = r1+1, 10
    while r2 != right + 2:
        if perm[r2] > perm[r1]:
            if perm[r2] < lo: lo, save = perm[r2], r2
        r2 += 1

    perm[r1], perm[save] = perm[save], perm[r1]
    perm = perm[0:r1+1] + sorted(perm[r1+1:])
    num = int(''.join(str(n) for n in perm))

    return num if check_prime(num) else 0

def find_prime():
    global perm, right
    m, n = 0, 9

    while n > 0:
        perm = [x for x in range(1, n+1)]
        right = len(perm) - 2

        while perm != [x for x in range(n, 0, -1)]: m = max(m, get_perm())
        
        if m != 0: break
        n -= 1

    return m

print('Prime:', find_prime())
