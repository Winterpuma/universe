from math import sqrt

# r^2 + m^2 = R^2

for r in range(1, 11):
    for m in range(1, 11):
        R = sqrt(r*r + m*m)
        if R % 1 == 0:
            print('r:', r, ' m:', m, ' R:', R)

