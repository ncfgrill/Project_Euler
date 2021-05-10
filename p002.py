################################################################################
#                         P2: Even Fibonacci numbers                           #
################################################################################
#                                                                              #
#    By considering the terms in the Fibonacci sequence whose values do not    #
#         exceed four million, find the sum of the even-valued terms.          #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

s = 0
d1, d2, = 1, 1
d3 = d1 + d2

while d3 < 4*(10**6):
    if d3 % 2 == 0:
        s += d3
    d1, d2 = d2, d3
    d3 = d1 + d2

print('Sum:', s)
