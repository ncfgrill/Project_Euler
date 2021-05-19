################################################################################
#                             P44: Pentagon numbers                            #
################################################################################
#                                                                              #
#   Find the pair of pentagonal numbers, P_j and P_k, for which their sum and  #
#    difference are pentagonal and D = |P_k - P_j| is minimized; what is the   #
#                                  value of D?                                 #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

from math import inf

pents = {n : (n * (3*n - 1)) // 2 for n in range(1, 2501)}
pents_set = set(pents.values())

def pent_dist(p):
    global pents, pent_set

    s, d = pents[p[1]] + pents[p[0]], pents[p[1]] - pents[p[0]]
    return d if s in pents_set and d in pents_set else inf

print('D:', min(map(pent_dist, [(j, k) for j in range(1, len(pents) - 1)\
                                       for k in range(j+1, len(pents))])))
