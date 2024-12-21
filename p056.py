################################################################################
#                            P56: Powerful digit sum                           #
################################################################################
#                                                                              #
#  Considering natural numbers of the form, a^b, where a, b < 100, what is the #
#                               maximum digit sum?                             #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

max_sum = 0
    
for a in range(2, 100):
    for b in range(2, 100):
        max_sum = max(max_sum, sum(int(l) for l in str(a ** b)))

print('Maximum digit sum:', max_sum)
