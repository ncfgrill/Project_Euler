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

names = []
letters = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7,
           'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14,
           'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21,
           'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

def read_file():
  global names
  f = open("p022_names.txt", "r")
  names = f.readline().split(',')
  names.sort()
  f.close()

def get_sum():
  total = 0
  for n in range(len(names)):
    s, i = 0, 1
    while names[n][i] != '"':
      s += letters[names[n][i]]
      i += 1
    total += s * (n+1)
  return total

def get_total():
  read_file()
  print('Total:', get_sum())

get_total()
