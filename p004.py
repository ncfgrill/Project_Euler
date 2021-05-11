################################################################################
#                       P4: Largest palindrome product                         #
################################################################################
#                                                                              #
#   Find the largest palindrome made from the product of two 3-digit numbers.  #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

i, hi = 100, 0

while i < 1000:
    j = 100
    while j < 1000:
        p = i * j
        if p > hi and str(p) == str(p)[::-1]: hi = p
        j += 1
    i += 1

print('Largest palindrome:', hi)
