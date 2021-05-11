################################################################################
#                          P26: Reciprocal cycles                              #
################################################################################
#                                                                              #
#    Find the value of d < 1000 for which 1/d contains the longest recurring   #
#                   cycle in its decimal fraction part.                        #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

d, save_diff, save_d = 2, 0, 0

while d < 1000:
    l, i = {}, 0
    while True:
        m = (10 ** i) % d
        if m not in l:
            l[m] = i
            i += 1
            continue
        diff = i - l[m]
        break

    if diff > save_diff: save_diff, save_d = diff, d
    d += 1

print('d:', save_d)
