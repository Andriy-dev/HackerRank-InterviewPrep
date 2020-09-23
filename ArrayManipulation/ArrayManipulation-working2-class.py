#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
from VectorOperations import Vector

def arrayManipulation(n, queries): 
                
    queries=[Vector(x[0],x[1],x[2]) for x in queries]
    remaining=[]
    
    if __debug__:
        print("Getting n={} queries={}".format(n,queries))

    while len(queries)>0:
        if __debug__:
            print("Starting OUTER round with queries={} and remaining={}".format(queries,remaining))
        q1=queries.pop()
        if __debug__:
            print("Just popped. queries={} q1={}".format(queries,q1))
            print("q1={}".format(q1))
        intersect_happens=False
        if __debug__:
            print("Will walk over {}".format(queries))
        
        processed_queries=[]
        while len(queries)>0:
            q2=queries.pop()
            if __debug__:
                print("Starting INNER round. len(queries)={} , queries={}, q1={} will intersect with q2={}".format(len(queries),queries,q1,q2))
           
            [l,m,r]=q1.intersect(q2)
            if not ( m==Vector(0,0,0) ):
                if __debug__:
                    print("Found intersection between {} and {} = {}".format(q1,q2,m))
                    print("Remaining l={} r={}".format(l,r))
                intersect_happens=True
                if not ( l==Vector(0,0,0) ):
                    queries.append(l)
                if not ( r==Vector(0,0,0) ):
                    queries.append(r)
                queries.append(m)
                if __debug__:
                    print("Now queries looks like: {}".format(queries))
                break
            else:
                if __debug__:
                    print("No intersections found between {} and {}".format(q1,q2))
                    print("Adding q2={} to processed_queries".format(q2))
                processed_queries.append(q2)
                if __debug__:
                    print("Now processed_queries looks like {}".format(processed_queries))
        if __debug__:
            print("We are at the end of the cycle")
            print("intersect_happens={}".format(intersect_happens))
            print("queries={}".format(queries))
            print("processed_queries={}".format(processed_queries))
            print("remaining={}".format(remaining))
        
        if not intersect_happens:
            remaining.append(q1)
            if __debug__:
                print("We added to remaining since intersect_happens is True ; remaining={}".format(remaining))
        queries=queries + processed_queries  
        if __debug__:
            print("After append: queries={}".format(queries))    
            print("="*60)
    return (max([x.weight for x in remaining]))
       
        
            
if __name__ == '__main__':

    queries=[[1,2,100],[2,5,100],[3,4,100]]
    n=5
    # expected 200
    print(arrayManipulation(n,queries))
    
    queries=[[1, 5, 3],[4, 8, 7],[6, 9, 1]]
    n=10
    # expected 10
    print(arrayManipulation(n,queries))

    f = open("input07-q.txt")
    n,m=10000000,100000
    queries=[]
    for q in f:
        queries.append(list(map(int,q.split())))

    print(arrayManipulation(n, queries))
    
