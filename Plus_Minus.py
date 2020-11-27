# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = [x for x in arr if x > 0]
    neg = [x for x in arr if x < 0]
    zr = [x for x in arr if x == 0]

    a = len(pos)/len(arr)
    b = len(neg)/len(arr)
    c = len(zr)/len(arr)

    reuslt = '%.6f'%a,'%.6f'%b,'%.6f'%c

    return reuslt

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    data = plusMinus(arr)
    print(data[0])
    print(data[1])
    print(data[2])
