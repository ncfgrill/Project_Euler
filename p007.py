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

def get_prime():
  i = 2
  p = 3
  while True:
    if check_prime(p):
      i += 1
      if i == 10002:
        break
    p += 2

  return p

print('10001st prime:', get_prime())
