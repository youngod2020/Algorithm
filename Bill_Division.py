#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    del bill[k]
    if (b - int(sum(bill) / 2)) == 0:
        print('Bon Appetit')
    else:
        pay = b - sum(bill) / 2
        print('%.f' % pay)


if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
