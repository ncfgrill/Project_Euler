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

import math

def check_prime(num):
  if num <= 3:
    return num > 1
  if num % 6 != 1 and num % 6 != 5:
    return False
  for i in range(2, math.ceil(math.sqrt(num)) + 1):
    if num % i == 0:
      return False

  return True

def sum_primes():
  s = 2
  p = 3

  while p < 2000000:
    if check_prime(p):
      s += p
    p += 2

  return s

print('Sum:', sum_primes())
