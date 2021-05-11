################################################################################
#                               P22: Names scores                              #
################################################################################
#                                                                              #
#                The score of a name is its place alphabetically               #
#           multipled by the sum of its letters (A = 1, B = 2, etc.).          #
#             What is the total of all the name scores in the file?            #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

num, base = 0, ord('A') - 1

def get_sum(name):
    global num, base

    s, i = 0, 1
    while name[i] != '"':
        s += ord(name[i]) - base
        i += 1

    num += 1
    return s * num

with open('p022_names.txt', 'r') as f:
    names = f.readline().split(',')
    names.sort()
    print('Total:', sum(map(get_sum, names)))
