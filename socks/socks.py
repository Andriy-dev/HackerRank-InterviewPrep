#!/bin/python

import math
import os
import random
import re
import sys
import sockMerchant as sockMerchant

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant.sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
