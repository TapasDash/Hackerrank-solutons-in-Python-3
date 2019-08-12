#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort() #it will sort the array
    mini = sum(arr[0:4])
    maxi = sum(arr[1:5])
    print(mini,maxi,end = '')
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
