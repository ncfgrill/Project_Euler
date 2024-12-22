################################################################################
#                         P63: Powerful Digit Counts                           #
################################################################################
#                                                                              #
#    The 5-digit number, 16807 = 7^5, is also a fifth power. Similary, the     #
#              9-digit number, 134217728 = 8^9, is a ninth power.              #
#                                                                              #
#    How many n-digit positive integers exist which are also an nth power?     #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

def find_total():
    total, i = set(), 1

    while True:
        for j in range(1, 10):
            num = j ** i
            num_len = len(str(num))

            if num_len == i: total.add(num)
            elif num_len > i: break
            else:
                if j == 9: return len(total)
        i += 1

print('Total:', find_total())
