################################################################################
#                               P15: Lattice paths                             #
################################################################################
#                                                                              #
#             How many such routes are there through a 20x20 grid?             #
#   (You can only move right and down from upper left to lower right corner.)  #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

# 40 choose 20
d, n, c = 40, 20, 1

while d > n:
  c *= d
  d -= 1

while n > 1:
  c //= n
  n -= 1

print('Routes:', c)
