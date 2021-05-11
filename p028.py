################################################################################
#                        P28: Number spiral diagonals                          #
################################################################################
#                                                                              #
#   What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral?  #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

c = 0

def sum_diag(n):
    global c

    c += 2
    return n**2 + (n**2 - c) + ((n-1)**2 + 1) + (n**2 - c*3)

print('Sum:', 1 + sum(map(sum_diag, [n for n in range(3,1003,2)])))
