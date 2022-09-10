#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    leaderboard = sorted(set(ranked), reverse = True)
    l = len(leaderboard)
    # print(l,leaderboard)
    res = []
    for a in player:
        while (l > 0) and (a >= leaderboard[l-1]):
            l -= 1
        res.append(l+1)
    return res

if __name__ == '__main__':
    ranked = list(map(int, input().rstrip().split()))

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print("\n".join(map(str,result)))
