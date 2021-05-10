################################################################################
#                            P30: Digit fifth powers                           #
################################################################################
#                                                                              #
#    Find the sum of all the numbers that can be written as the sum of fifth   #
#                            powers of their digits.                           #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

def calculate(num):
  s = 0
  for i in num:
    s += int(i) ** 5
  return s

def find_fifths():
  s = 0
  for d in range(10, 1000000):
    if d == calculate(str(d)):
      s += d
  return s

print('Sum:', find_fifths())
