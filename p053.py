################################################################################
#                         P53: Combinatoric Selections                         #
################################################################################
#                                                                              #
#        There are exactly ten ways of selecting three from five, 12345:       #
#               123, 124, 125, 134, 135, 145, 234, 235, 245, 345               #
#                                                                              #
#  How many, not necessarily distinct, values of n choose r for 1 <= n <= 100, #
#                         are greater than one-million?                        #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

from math import factorial

def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

def find_values():
    values, n = 0, 1

    while n <= 100:
        for r in range(1, n+1):
            if choose(n, r) > 1000000: values += 1

        n += 1

    return values

print('Values greater than one-million:', find_values())
