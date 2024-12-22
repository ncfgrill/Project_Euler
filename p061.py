################################################################################
#                        P61: Cyclical Figurate Numbers                        #
################################################################################
#                                                                              #
# Find the sum of the only ordered set of six cyclic 4-digit numbers for which #
#  each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal,   #
#       and octagonal, is represented by a different number in the set.        #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from numpy import roots

tria, squa, pent, hexa, hept, octa = [], [], [], [], [], []

def check_roots(r):
    r1, r2 = r[0], r[1]

    if r1 > 0 and int(r1) == r1:   return True
    elif r2 > 0 and int(r2) == r2: return True
    else:                          return False

def check_polygonal(num):
    if check_roots(roots([1, 1, -2*num])):  tria.append(num) # Triangular
    if check_roots(roots([1, 0, -1*num])):  squa.append(num) # Square
    if check_roots(roots([3, -1, -2*num])): pent.append(num) # Pentagonal
    if check_roots(roots([2, -1, -1*num])): hexa.append(num) # Hexagonal
    if check_roots(roots([5, -3, -2*num])): hept.append(num) # Heptagonal
    if check_roots(roots([3, -2, -1*num])): octa.append(num) # Octagonal

def find_polygonal():
    for i in range(1000, 10000):
        if str(i)[2] == '0': continue
        check_polygonal(i)

def check(nums, checked):
    if checked == 0b111111:
        if str(nums[0])[:2] == str(nums[-1])[2:]:
            print(nums, 'Sum:', sum(nums))
            return 1
    
    last_two = str(nums[-1])[2:]
    if not (checked & 0b10):
        for s in squa:
            if last_two == str(s)[:2]: check(nums + [s], checked + 0b10)
    if not (checked & 0b100):
        for p in pent:
            if last_two == str(p)[:2]: check(nums + [p], checked + 0b100)
    if not (checked & 0b1000):
        for h in hexa:
            if last_two == str(h)[:2]: check(nums + [h], checked + 0b1000)
    if not (checked & 0b10000):
        for h in hept:
            if last_two == str(h)[:2]: check(nums + [h], checked + 0b10000)
    if not (checked & 0b100000):
        for o in octa:
            if last_two == str(o)[:2]: check(nums + [o], checked + 0b100000)
    return 0

def find_sequence():
    find_polygonal()

    for t in tria:
        if check([t], 0b1): break

find_sequence()
