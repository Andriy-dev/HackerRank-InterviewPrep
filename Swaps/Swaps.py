#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	narr=list(map(lambda x: x-1,arr))
	ndict={ x[1]:x[0] for x in enumerate(narr) }
	swaps=0
	
	for location in sorted(ndict.values(),reverse=True):
	    if narr[location]!=location:
	        
	        position0=ndict[location] 
	        value0=location           
	        
	        position1=location    
	        value1=narr[location] 

	        ndict[value0]=position1 
	        ndict[value1]=position0 
	        
	        narr[position0]=value1 
	        narr[position1]=value0
	        
	        # updating swaps
	        swaps+=1
	
	return swaps

if __name__ == '__main__':

    arr=[7,1,3,2,4,5,6]

    print(minimumSwaps(arr))

    
    