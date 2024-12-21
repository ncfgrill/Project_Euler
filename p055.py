################################################################################
#                             P55: Lychrel numbers                             #
################################################################################
#                                                                              #
#            How many Lychrel numbers are there below ten-thousand?            #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

total, found = 0, set()

for i in range(1, 10000):
    if i in found: continue

    save, n, num = [i], 0, i
    while n < 50:
        num += int(str(num)[::-1])
        if str(num) == str(num)[::-1]: break
        else: save.append(num)
        n += 1
    if n < 50: found.update(save)
    else: total += 1

print('Lychrel numbers below 10000:', total)
