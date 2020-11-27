# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == 'PM':
        if s[:2] != '12' :
            hour = str(int(s[:2]) + 12)
            change = s.replace(s[:2], hour)[:-2]
        else:
            change = s[:-2]
    else :
        if s[:2] == '12':
            change = s.replace(s[:2], '00')[:-2]
        else: 
            change = s[:-2]
            
    return change

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
