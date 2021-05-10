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
  if num <= 3:
    return num > 1
  if num % 6 != 1 and num % 6 != 5:
    return False
  for i in range(2, ceil(sqrt(num)) + 1):
    if num % i == 0:
      return False

  return True

def circle_num(num):
  num = num[1:] + num[0]
  return int(num)

def find_primes():
  primes = 1 # starting with 2
  for p in range(3, 1000000):
    if '0' in str(p) or '2' in str(p) or\
       '4' in str(p) or '6' in str(p) or '8' in str(p):
      continue
    if not check_prime(p):
      continue

    save = p
    c = save
    while True:
      c = circle_num(str(c))
      if c == save:
        break
      if not check_prime(c):
        break

    if c == save:
      primes += 1

  return primes

print('Primes:', find_primes())
