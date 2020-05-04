#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    test = 2
    str1 = 'YES'
    str2 = 'NO'
    for item in range(0, len(s1)):
        if 1 < test and test < 10:
            if(s1[item] in s2):
                return str1
            else:
                return str2



        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()


      
