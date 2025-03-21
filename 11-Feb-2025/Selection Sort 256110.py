# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    ARRAY_LENGTH = 100
    nums = [0] * ARRAY_LENGTH
    
    for num in arr:
        nums[num] += 1
    
    nums = [str(freq) for freq in nums]
    return nums

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
