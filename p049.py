################################################################################
#                            P49: Prime permutations                           #
################################################################################
#                                                                              #
#   What 12-digit number do you form by concatenating the three terms in this  #
#                                  sequence?                                   #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import ceil, sqrt

def check_prime(num):
    if num % 6 != 1 and num % 6 != 5: return False

    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0: return False

    return True

def find_perm():
    for i in range(1001, 4001, 2):
        if i == 1487 or not check_prime(i): continue

        perms, check = [i], ''.join(sorted(str(i)))
        while len(perms) != 3:
            i += 3330
            if check_prime(i):
                if check != ''.join(sorted(str(i))): break
                perms.append(i)

        if len(perms) == 3: return ''.join(str(x) for x in perms)

print('Number:', find_perm())
