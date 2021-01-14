## 문제
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix arr is shown below:

# 123
# 456
# 989

# 1+5+9 = 15
# 3+5+9 = 17
# |15 - 17| = 2


## 정답
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
    r = []
    l = []
    for i in range(len(arr)):
        r.append(arr[i][i])

    for k, j in zip(range(len(arr)),range(len(arr)-1, -1, -1)):
        l.append(arr[k][j])

    result = abs(sum(r) - sum(l))
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
