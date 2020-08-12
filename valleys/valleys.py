#!/bin/python

import math
import os
import random
import re
import sys

# def verbosedebug(func):
#     def wrapper(*args,**kwargs):
#         original_result = func(*args,**kwargs)
#         print("Arguments :",args,kwargs)
#         print("Results:",original_result)
#         return original_result
#     return wrapper

#@verbosedebug
# Complete the countingValleys function below.
def countingValleys(n, s):
  valleys=0
  location=0

  for step in s:
	if step=="D":
		if location==0:
			valleys+=1
		location-=1
	else:
		location+=1
  return valleys

class TestClass:
    def test_one(self):
        n=8
        s="UDDDUDUU"
        assert countingValleys(n,s) == 1

    def test_two(self):
        n=10
        s="UDDDUDUUDU"
        assert countingValleys(n,s) == 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
