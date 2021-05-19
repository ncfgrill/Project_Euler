################################################################################
#                           P32: Pandigital products                           #
################################################################################
#                                                                              #
#  Find the sum of all products whose multiplicand/multiplier/product identity #
#                  can be written as a 1 through 9 pandigital.                 #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

def check_pan(m1, m2, p):
    return ''.join(sorted(m1 + m2 + p)) == '123456789'

def find_sum():
    prods = set()

    for i in range(1, 99):
        for j in range(123, 9877):
            p = i * j
            if check_pan(str(i), str(j), str(p)): prods.add(p)

    return sum(prods)

print('Sum:', find_sum());
