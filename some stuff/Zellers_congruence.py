# Zeller's congruence

from math import floor

days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
q = int(input('day '))
m = int(input('month ')) #3-march....13-jan, 14- feb
y = int(input('year '))

k = y%100
j = floor(y/100)
h = q + floor(13*(m+1)/5) + k + floor(k/4) + floor(j/4) - 2*j

print('this day was', days[h%7])
        
