################################################################################
#                            P52: Permuted Multiples                           #
################################################################################
#                                                                              #
#    It can be seen that the number, 125874, and its double, 251748, contain   #
#              exactly the same digits, but in a different order.              #
#                                                                              #
#   Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,   #
#                            contain the same digit.                           #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

from itertools import permutations

def check_multiples(n):
    perms = set(''.join(p) for p in permutations(n))

    for m in range(2,7):
        if str(m * int(n)) not in perms: return False

    return True

def find_integer():
    curr_int = 1

    while not check_multiples(str(curr_int)):
        curr_int += 1

    return curr_int

print('Smallest positive integer:', find_integer())
