################################################################################
#                        P24: Lexicographic permutations                       #
################################################################################
#                                                                              #
#      What is the millionth lexicographic permutation of the digits 0-9?      #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

perm = [0,1,2,3,4,5,6,7,8,9]
i, right = 1, len(perm) - 2

while i != 1000000:
  r1 = right
  while True:
    if perm[r1] < perm[r1+1]:
      break
    r1 -= 1

  r2 = r1+1
  lo = 10
  while r2 != right + 2:
    if perm[r2] > perm[r1]:
      if perm[r2] < lo:
        lo = perm[r2]
        save = r2
    r2 += 1

  perm[r1], perm[save] = perm[save], perm[r1]
  sub = perm[r1+1:]
  sub = sorted(sub)
  perm = perm[0:r1+1] + sub
  i += 1

print('Permutation:', perm)
