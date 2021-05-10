################################################################################
#                         P6: Sum square difference                            #
################################################################################
#                                                                              #
#  Find the difference between the sum of the squares of the first one hundred #
#                 natural numbers and the square of the sum.                   #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

n = 100

sum_of_sq = (n * (n + 1) * (2*n + 1)) // 6
sq_of_sum = (((n + 1) * n) // 2) ** 2

print('Difference:', sq_of_sum - sum_of_sq)
