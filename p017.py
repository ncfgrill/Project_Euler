################################################################################
#                           P17: Number letter counts                          #
################################################################################
#                                                                              #
#  If all the numbers from 1 to 1000 (one thousand) inclusive were written out #
#                   in words, how many letters would be used?                  #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

ones = {1 : 3, 2 : 3, 3 : 5, 4 : 4, 5 : 4, 6 : 3, 7 : 5, 8 : 5, 9 : 4}
tens = {10 : 3, 11 : 6, 12 : 6, 13 : 8, 14 : 8, 15 : 7, 16 : 7, 17 : 9, 18 : 8,
        19 : 8, 2 : 6, 3 : 6, 4 : 5, 5 : 5, 6 : 5, 7 : 7, 8 : 6, 9 : 6}
hundred = 7

n, s = 1, 0
while n < 1000:
    a, b = n % 100, n // 100
    if a != 0:
        if a < 10:   s += ones[a]
        elif a < 20: s += tens[a]
        else:
            c = a // 10
            if c != 0: s += tens[c]
            a %= 10
            if a != 0: s += ones[a]
    if b != 0:
        s += ones[b]
        s += hundred
    n += 1

# Add 'and' for each number 100-999 excluding base values (100, 200, etc.)
s += (99 * 9 * 3)

# Add 'one thousand'
s += 11

print('Sum:', s)
