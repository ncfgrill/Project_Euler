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

def check_palindrome(num):
    return num == num[::-1]

def find_pal():
    i, hi = 100, 0

    while i < 1000:
        j = 100
        while j < 1000:
            p = i * j
            if p > hi and check_palindrome(str(p)): hi = p
            j += 1
        i += 1

    return hi

print('Largest palindrome:', find_pal())
