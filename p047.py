################################################################################
#                         P47: Distinct primes factors                         #
################################################################################
#                                                                              #
# Find the first four consecutive integers to have four distinct prime factors #
#                 each. What is the first of these numbers?                    #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import ceil, sqrt

nums, all_factors = [], set()

def check_prime(num):
    if num <= 3:                        return num > 1
    elif num % 6 != 1 and num % 6 != 5: return False
    
    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0: return False

    return True

def get_pf(d):
    s = set()
    for i in list(d.items()): s.add(i[0] ** i[1])

    return s

def find_factors(num):
    factors = {}
    
    for f1 in range(2, num + 1):
        if num == 1: break
        while num > 1 and num % f1 == 0:
            if check_prime(f1):
                if f1 not in factors: factors[f1] = 1
                else:                 factors[f1] = factors[f1] + 1
                num //= f1

    return get_pf(factors)

def consecutive():
    global nums, all_factors
    n = 2

    while len(nums) < 4:
        n_f = find_factors(n)
        if len(n_f) != 4 or all_factors & n_f != set():
            nums.clear()
            all_factors.clear()
        else:
            nums.append(n)
            all_factors.update(n_f)
        n += 1

    return nums[0]

print('Number:', consecutive())
