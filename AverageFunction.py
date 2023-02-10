#!/bin/python3

import os


# write your code here
def find_average(*args):
    if len(args) > 100 or len(args) < 1:
        return
    if max(args) > 100 or min(args) < -100:
        return
    return sum(args) / len(args)


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    res = find_average(*nums)
    print(res)
