################################################################################
#                            P52: Permuted multiples                           #
################################################################################
#                                                                              #
#    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x   #
#                            contain the same digits.                          #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from datetime import datetime

start = datetime.now()

num = 1

while True:
    compare, tf = ''.join(sorted(str(num))), True

    for i in range(2, 7):
        if ''.join(sorted(str(i * num))) != compare:
            tf = False
            break

    if tf: break
    num += 1

print('Integer:', num)
print(datetime.now() - start)
