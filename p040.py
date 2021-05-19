################################################################################
#                         P40: Champernowne's constant                         #
################################################################################
#                                                                              #
#   If d_n represents the nth digit of the fractional part, find the value of  #
#                         the following expression.                            #
#         d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000         #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

c, i = '', 1
while len(c) < 1000000:
    c += str(i)
    i += 1

print('Value:', int(c[0]) * int(c[9]) * int(c[99]) * int(c[999]) *\
        int(c[9999]) * int(c[99999]) * int(c[999999]))
