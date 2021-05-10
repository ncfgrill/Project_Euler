################################################################################
#                        P46: Golbach's other conjecture                       #
################################################################################
#                                                                              #
#   What is the smallest odd composite that cannot be written as the sum of a  #
#                           prime and twice a square?                          #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import ceil, sqrt

def check_prime(num):
  if num <= 3:
    return num > 1
  if num % 6 != 1 and num % 6 != 5:
    return False
  for i in range(2, ceil(sqrt(num)) + 1):
    if num % i == 0:
      return False

  return True

def find_composite():
  n = 9
  while True:
    if not check_prime(n):
      p, s = 0, 1
      while 2 * (s ** 2) <= n - 3:
        c = n - 2 * (s ** 2)
        if check_prime(c):
          p = 1
          break
        s += 1
      if p == 0:
        break
    n += 2

  return n

print('Composite:', find_composite())
