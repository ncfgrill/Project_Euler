################################################################################
#                          P42: Coded triangle numbers                         #
################################################################################
#                                                                              #
#        Using p042_words.txt, how many given words are triangle words?        #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

tri_nums, base = [], ord('A') - 1

def get_tri():
    global tri_nums
    for n in range(1, 101): tri_nums.append(n*(n+1)//2)

def get_total(word):
    global base

    s, i = 0, 1
    while word[i] != '"':
        s += ord(word[i]) - base
        i += 1
    return 1 if s in tri_nums else 0

def read_file():
    with open('p042_words.txt', 'r') as f:
        words = f.readline().split(',')
        return sum(list(map(get_total, words)))

get_tri()
print('Total:', find_total())
