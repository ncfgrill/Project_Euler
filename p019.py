################################################################################
#                             P19: Counting Sundays                            #
################################################################################
#                                                                              #
# How many Sundays fell on the first of the month during the twentieth century #
#                          (1 Jan 1901 to 31 Dec 2000)?                        #
#                                                                              #
################################################################################
#                       Problem found at projecteuler.net                      #
#                                Author: ncfgrill                              #
################################################################################

# Sunday will be represented as day 0
year, month, day, total = 1901, 1, 366 % 7, 0
days31 = [1, 3, 5, 7, 8, 10, 12]
days30 = [4, 6, 9, 11]

while year < 2001:
  if day == 0:
    total += 1

  if month in days31:
    day += 31
  elif month in days30:
    day += 30
  else: # February...
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
      day += 29
    else:
      day += 28

  if month == 12:
    month = 1
    year += 1
  else:
    month += 1
  day %= 7

print('Sundays:', total)
