import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # idea
    '''
        for n element at the start of first line indent n-1 space and then slowly each line
    '''
    for line in range(n,0, -1):
        str = '#'*(n - (line - 1))
        print(str.rjust(n))



if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)