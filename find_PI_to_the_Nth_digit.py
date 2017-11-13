from mpmath import *

def find_pi(digit):
    mp.dps = digit + 1
    print(pi)

find_pi(3)
find_pi(300)
