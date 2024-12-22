################################################################################
#                            P65: Convergents of e                             #
################################################################################
#                                                                              #
#    Find the sum of digits in the numerator of the 100th convergent of the    #
#                          continued fraction for e.                           #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

e = []

def get_convergents():
    global e
    i = 1

    while len(e) < 99:
        e += [1, 2*i, 1]
        i += 1

def find_100th():
    get_convergents()

    n = 2
    n_1 = 1
    for c in e:
        n_1, n_2 = n, n_1
        n = n_1 * c + n_2
    return sum([int(x) for x in str(n)])

print('Sum of digits of 100th convergent of e:', find_100th())
