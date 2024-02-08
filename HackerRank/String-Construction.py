# Complete the stringConstruction function in the editor below. It should return the minimum cost of copying a string.
# stringConstruction has the following parameter(s)

# Given n strings s[i], find and print the minimum cost of copying each s[i] to p[i] on a new line.

# For example, given a string s = abcabc , it can be copied for 3 dollars. Start by copying a, b,  and c individually at a cost of 1 dollar per character. 
# String  p = abc at this time. Copy p[0:2] to the end of p at no cost to complete the copy.
EX:-  
# INPUT : 2        OUTPUT :- 4
#         abcd               2
#         abab

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    # Write your code here
    set1 = set(s)
    return len(set1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
