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

prods = set()

def check_pan(m1, m2, p):
    return ''.join(sorted(m1 + m2 + p)) == '123456789'

def find_sum(n):
    p = n[0] * n[1]
    if check_pan(str(n[0]), str(n[1]), str(p)) and p not in prods:
        prods.add(p)
        return p
    return 0

print('Sum:',
      sum(map(find_sum,
              [(i, j) for i in range(1, 99) for j in range(123, 9877)])));
