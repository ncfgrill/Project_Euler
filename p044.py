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

pent_set = set()
pent_list = []

def calc_pents():
  n = 1
  while n <= 2500:
    p = (n * (3*n - 1)) // 2
    pent_set.add(p)
    pent_list.append(p)
    n += 1

def minimize():
  global pent_set, pent_list
  dist = inf

  for j in range(len(pent_list) - 2):
    for k in range(j+1, len(pent_list) - 1):
      s, d = pent_list[k] + pent_list[j], pent_list[k] - pent_list[j]
      if s in pent_set and d in pent_set and d < dist:
        dist = d

  return dist

calc_pents()
print('D:', minimize())
