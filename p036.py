################################################################################
#                         P36: Double-base palindromes                         #
################################################################################
#                                                                              #
# Find the sum of all numbers, less than one million, which are palindromic in #
#                              base 10 and base 2.                             #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

def find_palindromes(n):
    b = bin(n)
    return n if str(n) == str(n)[::-1] and b[2:] == b[:1:-1] else 0

# Only check odd numbers as even numbers always begin with 1 and end with 0
print('Sum:', sum(map(find_palindromes, [x for x in range(1,1000000,2)])))
