################################################################################
#                         P39: Integer right triangles                         #
################################################################################
#                                                                              #
#      For which value of p ≤ 1000, is the number of solutions maximized?      #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import sqrt

perimeters, a = {}, 1

while 2*a + sqrt(2 * a**2) <= 1000:
    b = a
    while True:
        c = sqrt(a**2 + b**2)
        p = a + b + c
        
        if p > 1000: break
        if c % 1 == 0:
            if p in perimeters: perimeters[p] = perimeters[p] + 1
            else:               perimeters[p] = 1
        b += 1
    a += 1

perimeters = sorted(perimeters.items(), key=lambda kv: kv[1], reverse=True)
print('Perimeter:', perimeters[0][0])
