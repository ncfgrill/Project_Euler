################################################################################
#                            P23: Non-abundant sums                            #
################################################################################
#                                                                              #
# Find the sum of all the positive integers which cannot be written as the sum #
#                           of two abundant numbers.                           #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

from math import ceil, sqrt

abundant, two_abun = [12], set()

def find_factors_sum(num):
    factors = {1}

    for f1 in range(2, ceil(sqrt(num)) + 1):
        if num % f1 == 0:
            f2 = num // f1
            factors.add(f1)
            factors.add(f2)
    return sum(factors)

def get_abundant():
    n = 13
    while n <= 28111:
        if n < find_factors_sum(n): abundant.append(n)
        n += 1

def get_two_abundant():
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            if abundant[i] + abundant[j] > 28123: break
            two_abun.add(abundant[i]+abundant[j])

get_abundant()
get_two_abundant()

print('Sum:', sum(x for x in range(1, 28124) if x not in two_abun))
