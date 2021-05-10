################################################################################
#                      P9: Special Pythagorean triplet                         #
################################################################################
#                                                                              #
#   There exists exactly one Pythagorean triplet for which a + b + c = 1000.   #
#                            Find the product abc.                             #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

def find_trip():
    a = 1

    while True:
        b = a + 1
        c = 1000 - a - b
        while b < c:
            if a ** 2 + b ** 2 == c ** 2:
                print('a =', a, 'b =', b, 'c =', c)
                return a * b * c
            b += 1
            c = 1000 - a - b
        a += 1

print('a*b*c =', find_trip())
