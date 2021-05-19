################################################################################
#                         P43: Sub-string divisibility                         #
################################################################################
#                                                                              #
#   For the numbers written with the digits 0-9, with d_1 denoting the first   #
#      digit, d_2 denoting the second digit, etc., find the sum of all 0-9     #
#               pandigital numbers with the following properties:              #
#                                                                              #
#       d_2-4 div 2; d_3-5 div 3; d_4-6 div 5; d_5-7 div 7; d_6-8 div 11       #
#                        d_7-9 div 13; d_8-10 div 17                           #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

perm = [0,1,2,3,4,5,6,7,8,9]
right = len(perm) - 2

def check():
    global perm

    p = ''.join(str(n) for n in perm)
    return int(p[2:5]) % 3 == 0 and int(p[4:7]) % 7 == 0 and\
           int(p[5:8]) % 11 == 0 and int(p[6:9]) % 13 == 0 and\
           int(p[7:]) % 17 == 0

def get_perm():
    global right, perm
    
    r1 = right
    while perm[r1] >= perm[r1+1]: r1 -= 1

    r2, lo = r1+1, 10
    while r2 != right + 2:
        if perm[r2] > perm[r1]:
            if perm[r2] < lo: lo, save = perm[r2], r2
        r2 += 1

    perm[r1], perm[save] = perm[save], perm[r1]
    perm = perm[0:r1+1] + sorted(perm[r1+1:])
    if perm[3] % 2 != 0 or perm[5] % 5 != 0: return 0

    return int(''.join(str(n) for n in perm)) if check() else 0

def sum_perms():
    global perm
    s = 0

    while perm != [9,8,7,6,5,4,3,2,1,0]: s += get_perm()

    return s

print('Sum:', sum_perms())
