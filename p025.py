################################################################################
#                       P25: 1000-digit Fibonacci number                       #
################################################################################
#                                                                              #
#   What is the index of the first term in the Fibonacci sequence to contain   #
#                                 1000 digits?                                 #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

a, b, n = 1, 1, 2

while True:
  c = a + b
  n += 1
  if len(str(c)) >= 1000:
    break
  a, b = b, c

print('Index:', n)

