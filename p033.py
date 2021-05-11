################################################################################
#                        P33: Digit cancelling fractions                       #
################################################################################
#                                                                              #
#  If the product of these four fractions is given in its lowest common terms, #
#                       find the value of the denominator.
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import prod

fractions = []

for n in range(10, 100):
    for d in range(n+1, 100):
        if n % 10 == 0 and d % 10 == 0: continue
        save, a, b = n / d, str(n), str(d)

        if a[0] == b[0]:   a, b = int(a[1]), int(b[1])
        elif a[0] == b[1]: a, b = int(a[1]), int(b[0])
        elif a[1] == b[0]: a, b = int(a[0]), int(b[1])
        elif a[1] == b[1]: a, b = int(a[0]), int(b[0])
        else:              continue

        if b != 0 and save == a / b: fractions.append((n, d))

print('Denominator:', prod(f[1]/f[0] for f in fractions))                              
