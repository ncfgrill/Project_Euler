################################################################################
#                            P29: Distinct powers                              #
################################################################################
#                                                                              #
# How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 #
#                              and 2 ≤ b ≤ 100?                                #
#                                                                              #
################################################################################
#                     Problem found at projecteuler.net                        #
#                              Author: ncfgrill                                #
################################################################################

print('Terms:', len({a**b for a in range(2,101) for b in range(2,101)}))
