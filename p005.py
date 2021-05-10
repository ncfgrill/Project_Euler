################################################################################
#                          P5: Smallest multiple                               #
################################################################################
#                                                                              #
#   What is the smallest positive number that is even divisible by all of the  #
#                          numbers from 1 to 20?                               #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

div = [20, 19, 18, 17, 16, 15, 14, 13, 11]
initial = 20 * 19 * 17 * 13 * 11
n = initial

while True:
    check = 0
    for d in div:
        if n % d != 0:
            n += initial
            break
        else: check += 1
    if check == len(div): break

print('Smallest positive number:', n)
