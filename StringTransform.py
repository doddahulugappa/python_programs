#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here
    if len(sentence) > 100 or len(sentence) < 1:
        return
    result_string = ""
    split_sentence = sentence.split()
    output_array = []
    for word in split_sentence:
        tmp = word[0]
        for i in range(1, len(word)):
            if ord(word[i].lower()) > ord(word[i - 1].lower()):
                tmp += word[i].upper()
            elif ord(word[i].lower()) == ord(word[i - 1].lower()):
                tmp += word[i]
            else:
                tmp += word[i].lower()
        output_array.append(tmp)
    return " ".join(output_array)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
