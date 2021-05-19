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

from math import factorial as fact

print('Sum:',
      sum(map(lambda s: s if s == sum(fact(int(d)) for d in str(s)) else 0,
              [x for x in range(10, 100000)])))
