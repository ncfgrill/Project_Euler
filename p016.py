################################################################################
#                             P16: Power digit sum                             #
################################################################################
#                                                                              #
#              What is the sum of the digits of the number 2^1000?             #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

print('Sum:', sum([int(d) for d in str(2**1000)]))
