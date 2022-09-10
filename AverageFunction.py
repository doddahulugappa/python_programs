#!/bin/python3

import math
import os
import random
import re
import sys


# write your code here
def find_average(*args):
    if len(args) > 100 or len(args) < 1:
        return
    if max(args) > 100 or min(args) < -100:
        return
    return sum(args) / len(args)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list(map(int, input().split()))
    res = find_average(*nums)

    fptr.write('%.2f' % res + '\n')

    fptr.close()