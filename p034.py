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

def fact_sum(num):
    sub_sum = 0
    for j in str(num):
        if num < fact(int(j)): break
        sub_sum += fact(int(j))
    return num if num == sub_sum else 0

print('Sum:', sum(list(map(fact_sum, [x for x in range(10, 100000)]))))
