#!/bin/python3

import math
import os
import random
import re
import sys
import itertools as it
# Complete the solve function below.

def solve(arr):
    result = 0
    arrIndexes = list(range(1,len(arr)+1))
    # arrIndexes = [i+1 for i,x in enumerate(arr)]
    for combination in set(it.combinations(arrIndexes,2)):
        if combination[0] < combination[1] and arr[combination[0]-1]*arr[combination[1]-1] <= max(arr[combination[0]-1:combination[1]]):
            result = result + 1
    return result
                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
