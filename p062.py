################################################################################
#                           P62: Cubic Permutations                            #
################################################################################
#                                                                              #
#   The cube, 41063625 (345^3), can be permuted to produce two other cubes:    #
#   56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest   #
# cube which has exactly three permutations of its digits which are also cube. #
#                                                                              #
# Find the smallest cube for which exactly five permutations of its digits are #
#                                    cube.                                     #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

perms = {}

n = 346
while True:
    num = n ** 3
    str_num_ordered = ''.join(sorted(list(str(num))))

    if str_num_ordered in perms:
        seen = perms[str_num_ordered][0]
        if seen == 4:
            print('Smallest cube with five perms:', perms[str_num_ordered][1])
            break
        else: perms[str_num_ordered] = [seen + 1, perms[str_num_ordered][1]]
    else: perms[str_num_ordered] = [1, num]

    n += 1
