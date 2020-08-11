from __future__ import print_function
import math
import sys
from itertools import combinations
from itertools import permutations

def full_levels(nodes):
    full_levels = int(math.log(nodes + 1,2)) - 1

    return(full_levels)

def sum_of_all_costs_to_level(n):
    s=0
    for level in xrange(n + 1):
        cost = level
        s+=cost * 2**level
    return s

def max_cost(nodes):
    #levels=nodes-1
    cost=nodes*(nodes - 1)/2
    return cost   

def binary_combinations(level):
    if level==0:
        return ['0','1']
    else:
        previous_level=binary_combinations(level-1) 
        return [ x+y for x in previous_level for y in previous_level ]

def binary_combinations_of_next_level(current_level_binary_representation):
    c=[]
    for i in current_level_binary_representation:
        #print(i)
        if i=="1":
            c.append(binary_combinations(1))
        else:
            c.append(['00','00','00','00'])
         
    return permutations(c,len(current_level_binary_representation))


for combination in binary_combinations_of_next_level('01'):
    print(combination)

sys.exit()   

for i in xrange(0,10):   
    print("Level={}".format(i))
    for combination in binary_combinations(i):     
        print(combination)

sys.exit()

for i in xrange(1,5*10**4+1):
    fl = full_levels(i)
    on_levels = 2**(fl+1) - 1
    remaining = i - on_levels

    sum_of_all_elemets = sum_of_all_costs_to_level(fl) + (fl + 1)*remaining

    print('nodes={},full_levels={},remaining={},sum_of_all_elemets={},max_cost={},max_levels={}'.format(i,fl,remaining,sum_of_all_elemets,max_cost(i),i-1))
