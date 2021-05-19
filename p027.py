################################################################################
#                           P27: Quadratic primes                              #
################################################################################
#                                                                              #
# Find the product of the coefficients, a and b, for the quadratic expressions #
#    that produces the maximum number of primes for consecutive values of n,   #
#               starting with n = 0. (|a| < 1000 and |b| <= 1000)              #
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

def evaluate(n, a, b):
    return n**2 + a*n + b

def find_primes():
    most, save_a, save_b = 0, 0, 0
    for a in range(-999, 1000, 2):
        for b in range(-999, 1000, 2):
            m = abs(a) % abs(b) if abs(a) > abs(b) else abs(b) % abs(a)
            if m == 0: continue

            n, primes = 0, 0
            while True:
                if check_prime(evaluate(n, a, b)):
                    primes += 1
                    n += 1
                else: break
      
            if primes > most: most, save_a, save_b = primes, a, b
    return save_a * save_b

print('Coefficent product:', find_primes())
