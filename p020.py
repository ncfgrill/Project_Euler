################################################################################
#                            P20: Factorial digit sum                          #
################################################################################
#                                                                              #
#                 Find the sum of the digits in the number 100!                #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

from math import factorial

n, s = str(factorial(100)), 0

for d in n:
  s += int(d)

print('Sum:', s)