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
    return num if num == sum(int(x) ** 5 for x in str(num)) else 0

print('Sum:', sum(map(calculate, [d for d in range(10, 1000000)])))
