################################################################################
#                         P57: Square root convergents                         #
################################################################################
#                                                                              #
#   It is possible to show that the square root of two can be expressed as an  #
#                         infinite continued fraction.                         #
#                                                                              #
# In the first one-thousand expansions, how many fractions contain a numerator #
#                    with more digits than the denominator?                    #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

n, d, total, i = 3, 2, 0, 1

while i < 1001:
    if len(str(n)) > len(str(d)): total += 1
    n, d = n + 2 * d, n + d
    i += 1

print('Fractions:', total)
