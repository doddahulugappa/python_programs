# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    dict_sum = {}
    for i in range(len(A)):
        temp_sum_of_digits = 0
        num = A[i]
        while num:
            temp_sum_of_digits += num % 10
            num = num // 10
        dict_sum[i] = [temp_sum_of_digits, i]

    print(dict_sum)

    sum_of_two = {}
    for key, value in dict_sum.items():
        sum_of_two[value[0]] = value[1]

    print(sum_of_two)


A = [51, 71, 17, 42]
solution(A)


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
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
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
    fptr = open("timeconversion", 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
