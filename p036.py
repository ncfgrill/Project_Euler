################################################################################
#                         P36: Double-base palindromes                         #
################################################################################
#                                                                              #
# Find the sum of all numbers, less than one million, which are palindromic in #
#                              base 10 and base 2.                             #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

def check_palindrome(num):
  return num == num[::-1]

def to_binary(num):
  b = ''
  while num > 0:
    if num % 2 == 0:
      b = '0' + b
    else:
      b = '1' + b
    num //= 2

  return b

def find_palindromes():
  s = 0
  for d in range(1, 1000000):
    if not check_palindrome(str(d)):
      continue
    if not check_palindrome(to_binary(d)):
      continue
    s += d

  return s

print('Sum:', find_palindromes())
