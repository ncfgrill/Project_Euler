################################################################################
#                           P67: Maximum path sum II                           #
################################################################################
#                                                                              #
#       Find the maximum total from top to bottom of the given triangle.       #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

from copy import deepcopy

tri = []
with open('p067_triangle.txt') as f:
    for line in f.readlines():
        tri.append([int(n) for n in line.strip().split(' ')])

sum_tri = deepcopy(tri)

for l in range(len(sum_tri) - 1):
    for r in range(len(sum_tri[l])): sum_tri[l][r] = 0

l = len(sum_tri) - 1
while l > 0:
    for r in range(len(sum_tri[l])):
        if r < len(sum_tri[l]) - 1:
            s = sum_tri[l][r] + tri[l-1][r]
            if s > sum_tri[l-1][r]: sum_tri[l-1][r] = s
        if r > 0:
            s = sum_tri[l][r] + tri[l-1][r-1]
            if s > sum_tri[l-1][r-1]: sum_tri[l-1][r-1] = s

    l -= 1

print('Maximum total:', sum_tri[0][0])
