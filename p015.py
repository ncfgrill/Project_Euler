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

from math import prod

# d choose n
d, n = 40, 20

c = prod(i for i in range(d-n+1, d+1)) // prod(j for j in range(1, n+1))

print('Routes:', c)
