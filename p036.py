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

# Only check odd numbers as even numbers always begin with 1 and end with 0
print('Sum:',
      sum(map(lambda n: n if str(n) == str(n)[::-1] and\
              str(bin(n))[2:] == str(bin(n))[:1:-1] else 0,
              [x for x in range(1,1000000,2)])))
