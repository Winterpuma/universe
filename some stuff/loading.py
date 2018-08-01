import sys
import time

i = 0
n = 100

while i <= n:
    print('\rLoading...'+str(i), end='')
    time.sleep(0.1)
    i += 1

