#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    if max(arr) > 100 or min(arr) < -100:
        return
    count_positive, count_negative, count_zero = 0, 0, 0
    for item in arr:
        if item > 0:
            count_positive += 1
        elif item < 0:
            count_negative += 1
        else:
            count_zero += 1
    a = "{:.6f}".format(count_positive / len(arr))
    b = "{:.6f}".format(count_negative / len(arr))
    c = "{:.6f}".format(count_zero / len(arr))
    print(a + "\n" + b +"\n"+ c)
    return a + "\n" + b +"\n"+ c

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
