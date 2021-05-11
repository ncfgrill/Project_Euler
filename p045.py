################################################################################
#                  P45: Triangular, pentagonal, and hexagonal                  #
################################################################################
#                                                                              #
#  Find the next triangle number (greater than 40755) that is also pentagonal  #
#                                and hexagonal.                                #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

def get_tria(num):
    return num * (num + 1) // 2

def get_pent(num):
    return num * (3 * num - 1) // 2

def get_hexa(num):
    return num * (2 * num - 1)

def find_number():
    t, p, h = 286, 165, 143
    tria, pent, hexa = get_tria(t), get_pent(p), get_hexa(h)

    while True:
        if tria == pent and tria == hexa: break

        while tria < pent or tria < hexa:
            t += 1
            tria = get_tria(t)

        while pent < tria:
            p += 1
            pent = get_pent(p)

        while hexa < tria:
            h += 1
            hexa = get_hexa(h)

    return tria

print('Number:', find_number())
