# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    curr = arr[-1]
    
    for i in range(n - 1, 0, -1):
        
        if curr <= arr[i - 1]:
            arr[i] = arr[i - 1]
            print(*arr)
        else:
            arr[i] = curr
            break
    if arr[0] > curr:
        arr[0] = curr
        # print(curr)
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
