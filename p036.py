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

def to_binary(num):
    b = ''
    while num > 0:
        if num % 2 == 0: b = '0' + b
        else:            b = '1' + b
        num //= 2

    return b

def find_palindromes(num):
    binary = to_binary(num)
    return num if str(num) == str(num)[::-1] and binary == binary[::-1] else 0

# Only check odd numbers as even numbers always begin with 1 and end with 0
print('Sum:', sum(map(find_palindromes, [x for x in range(1,1000000,2)])))
