################################################################################
#                         P64: Odd Period Square Roots                         #
################################################################################
#                                                                              #
#       How many continued fractions for N <= 10000 have an odd period?        #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import floor, sqrt

def find_period(num):
    triplets = set()
    length = 0
    sr = sqrt(num)
    if floor(sr) == sr: return 0
    
    m_i, d_i, a_i = 0, 1, floor(sr)
    triplets.add((m_i, d_i, a_i))
    
    while True:
        m_n = d_i * a_i - m_i
        d_n = (num - m_n ** 2) / d_i
        a_n = floor((sr + m_n) / d_n)

        trip = (m_n, d_n, a_n)
        if trip in triplets: return length

        length += 1
        triplets.add(trip)
        m_i, d_i, a_i = m_n, d_n, a_n

def get_total():
    total = 0

    for i in range(10001):
        if find_period(i) % 2: total += 1
    
    return total

print('# of continued fractions with odd period:', get_total())
