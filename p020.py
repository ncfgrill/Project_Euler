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

print('Sum:', sum(int(d) for d in str(factorial(100))))
