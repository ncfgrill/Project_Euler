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
    for i in str(num): s += int(i) ** 5
    return num if num == s else 0

print('Sum:', sum(map(calculate, [d for d in range(10, 1000000)])))
