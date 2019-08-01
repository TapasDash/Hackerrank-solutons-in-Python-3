#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

def rotate(lst, x):
    x = -x
    d = deque(lst)
    d.rotate(x)
    return d

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    rotatedList = rotate(a,d)

    for i in rotatedList:
        print(i,end=" ")
