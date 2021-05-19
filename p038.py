################################################################################
#                           P38: Pandigital multiples                          #
################################################################################
#                                                                              #
#  What is the largest 1 to 9 pandigital 9-digit number that can be formed as  #
#     the concatented product of an integer with (1,2, ... ,n) where n > 1?    #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

def check_pan(p):
    return ''.join(sorted(p)) == '123456789'

def find_prod():
    upper, i, m = 987654321 ** 0.5, 1, -1

    while i < upper:
        i += 1
        if '0' in str(i): continue

        pd, j = '', 1
        while len(pd) < 9:
            p = i * j
            if '0' in str(p): break
            pd += str(p)
            j += 1

        if len(pd) == 9 and check_pan(pd): m = max(int(pd), m)

    return m

print('Pand:', find_prod())
