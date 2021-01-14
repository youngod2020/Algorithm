# Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:
# It is a concatenation of one or more words consisting of English letters.
# All letters in the first word are lowercase.
# For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

# Sample Input
# saveChangesInTheEditor
# Sample Output
# 5

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    cntup = 1
    for i in range(len(s)):
        if s[i].isupper() == True:
            cntup += 1            
    return cntup

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = camelcase(s)
    fptr.write(str(result) + '\n')
    fptr.close()
    
    
    
