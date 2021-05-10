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

words = []
letters = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7,
           'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14,
           'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21,
           'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
tri_nums = []

def read_file():
  global words
  f = open("p042_words.txt", "r")
  words = f.readline().split(',')
  f.close()

def get_tri():
  global tri_nums
  for n in range(1, 101):
    tri_nums.append(n*(n+1)//2)

def get_total():
  total = 0
  for n in range(len(words)):
    s, i = 0, 1
    while words[n][i] != '"':
      s += letters[words[n][i]]
      i += 1
    if s in tri_nums:
      total += 1
  return total

def find_total():
  read_file()
  get_tri()
  return get_total()

print('Total:', find_total())
