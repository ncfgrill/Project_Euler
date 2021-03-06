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

a, b, c, n = 1, 1, 2, 2

while len(str(c)) < 1000:
    c = a + b
    n += 1
    a, b = b, c

print('Index:', n)
