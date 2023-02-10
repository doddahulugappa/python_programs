


def staircase(n):
    # Write your code here
    for i in range(n):
        print(" "*(n-(i+1))+"#"*(i+1))
staircase(6)

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'time_conversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def time_conversion(s):
    # Write your code here
    if re.search(r"[01]\d:[0-5]\d:[0-5]\d[AP]M", s) is None:
        return

    if s[-2:] == "AM":
        if int(s[:2]) == 12:
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        if int(s[:2]) == 12:
            return s[:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:-2]


if __name__ == '__main__':
    fptr = open("time_conversion", 'w')

    s = input()

    result = time_conversion(s)

    fptr.write(result + '\n')

    fptr.close()
