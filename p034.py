################################################################################
#                             P34: Digit factorials                            #
################################################################################
#                                                                              #
#  Find the sum of all numbers which are equal to the sum of the factorial of  #
#       their digits. Note: Do not include 1! or 2! as they are not sums.      #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import factorial as f

s = 0
fact = [f(0), f(1), f(2), f(3), f(4), f(5), f(6), f(7), f(8), f(9)]

for i in range(10, 100000):
  sub_sum = 0
  for j in str(i):
    if i < fact[int(j)]:
      break
    sub_sum += fact[int(j)]
  if sub_sum == i:
    s += i

print('Sum:', s)
