#!/bin/python3




import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap = []
    org = []
    for i in range(len(apples)):
        ap.append(a + apples[i])
    for j in range(len(oranges)):
        org.append(b + oranges[j])
    a = [a for a in ap if (a >= s) & (a <= t)]
    b = [b for b in org if (b >= s) & (b <= t)]    
    
    return len(a), len(b)
    
if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    result = countApplesAndOranges(s, t, a, b, apples, oranges)
    print(result[0])
    print(result[1])
    
    
    
    
