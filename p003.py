################################################################################
#                          P3: Largest prime factor                            #
################################################################################
#                                                                              #
#              What is the largest prime factor of 600851475143?               #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import ceil, sqrt

def check_prime(num):
    if num <= 3:                        return num > 1
    elif num % 6 != 1 and num % 6 != 5: return False
    
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0: return False

  return True

def get_factor():
    d, factor, p = 600851475143, 1, 3
  
    while d != 1:
        if check_prime(p):
            while True:
                if d % p != 0: break
                d /= p
                factor = p
        p += 2

  return factor

print('Largest prime factor:', get_factor())
