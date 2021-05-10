################################################################################
#                         P14: Longest Collatz sequence                        #
################################################################################
#                                                                              #
#     Which starting point, under one million, produces the longest chain?     #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

vals = {}
n, hi = 2, 0

for i in range(2, 1000000):
  terms = 1
  n = i

  while n != 1:
    if n % 2 == 0:
      n //= 2
    else:
      n = 3*n + 1

    if n in vals:
      terms += vals[n]
      break
    terms += 1

  vals[i] = terms
  
  if terms > hi:
    hi = terms

vals = dict(sorted(vals.items(), key=lambda item: item[1], reverse = True))
nums = list(vals.keys())
print('Starting point:', nums[0])
