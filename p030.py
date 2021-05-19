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

print('Sum:',
      sum(map(lambda n: n if n == sum(int(c) ** 5 for c in str(n)) else 0,
              [d for d in range(10, 1000000)])))
