################################################################################
#                             P21: Amicable numbers                            #
################################################################################
#                                                                              #
#           Evaluate the sum of all the amicable numbers under 10000.          #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

from math import ceil, sqrt

def find_factors_sum(num):
    factors = [1]

    for f1 in range(2, ceil(sqrt(num)) + 1):
        if num % f1 == 0:
            f2 = num // f1
            if f1 not in factors: factors.append(f1)
            if f2 not in factors: factors.append(f2)
    if num in factors: factors.remove(num)
    return sum(factors)

def find_amicable():
    n, f_sum = 2, {1:0}
    while n < 10000:
        f_sum[n] = find_factors_sum(n)
        n += 1

    amicable, s = set(), 0
    for n1 in range(2, 10000):
        if n1 in amicable: continue
        n2 = f_sum[n1]
        if n1 == n2: continue
        if n2 < 10000 and n2 not in amicable:
            if f_sum[n2] == n1:
                amicable.add(n1)
                amicable.add(n2)
                s += n1 + n2
    return s

print('Sum:', find_amicable())
