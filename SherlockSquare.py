#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b


def squares(a, b):
    # Write your code
    numOfSquares = 0
    x = 1
    while x * x < a:
        x += 1
    while x * x <= b:
        numOfSquares += 1
        x += 1

    return numOfSquares


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)
        print(result)

