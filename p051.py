################################################################################
#                         P51: Prime digit replacements                        #
################################################################################
#                                                                              #
#      Find the smallest prime which, by replacing part of the number (not     #
#  necessarily adjacent digits) with the same digit, is part of an eight prime #
#                                  value family.                               #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

from copy import deepcopy
from math import ceil, sqrt

zero = 5

def check_prime(num):
    if num % 6 != 1 and num % 6 != 5: return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0: return False

    return True

def convert(num):
    return int(''.join(n for n in num))

def variations(num):
    global zero

    for i in range(1, 2 ** zero):
        primes, switch = 0, ('{:0'+ str(zero) + 'b}').format(i)
        if list(switch).count('1') % 3 != 0: continue
        
        for r in range(1, 10):
            save = deepcopy(num)
            for j in range(zero):
                if switch[j] == '1': save[j] = str(r)

            if check_prime(convert(save)): primes += 1
            if primes < r - 1: break
        if primes == 8:
            s = ''
            for k in range(len(num) - 1):
                if switch[k] == '1': s += '1'
                else:                s += num[k]
            s += num[-1]
            return s
            
    return -1

def find_prime():
    global zero

    n = '100001'
    while True:
        zero = len(n) - 1
        prime = variations(list(n))
        if prime != -1: return prime

        n = str(int(n) + 2)

print('Smallest prime:', find_prime())
