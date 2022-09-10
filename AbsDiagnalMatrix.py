#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    if any([(max(item) > 100 or min(item) < -100) for item in arr]):
        return
    principle_diagnol, secondary_diagnol = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                principle_diagnol += arr[i][j]
            if (i + j) / (len(arr) - 1) == 1:
                secondary_diagnol += arr[i][j]

    return abs(principle_diagnol - secondary_diagnol)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
