from __future__ import print_function

def minimumSwaps_v1(arr):
    swaps=0
    l=len(arr)
    while True:
        will_swap=False
        mx=None
        for i in range(l-1):
            for j in range(i+1,l):
                if arr[i] > arr[j]:
                    #candidate to swap
                    if not will_swap:
                        will_swap=True
                        mx=[i,j,j-i+arr[i]-arr[j]]
                        #print("Changing will_swap,{}-{}+{}-{} ".format(j,i,arr[i],arr[j]))
                    elif j-i+arr[i]-arr[j]>mx[2]:
                        #print("Updating mx,{}-{}+{}-{} , old value ()".format(j,i,arr[i],arr[j],mx))
                        mx=[i,j,j-i+arr[i]-arr[j]]
                        #print("Updating mx,{}-{}+{}-{} ".format(j,i,arr[i],arr[j]))
        if will_swap:
            print("Will Perform swap , {} over {} , {}".format(arr,mx,swaps))
            tmp_i=arr[mx[0]]
            arr[mx[0]]=arr[mx[1]]
            arr[mx[1]]=tmp_i
            swaps+=1
        else:
            print("Returning , {} {}".format(arr,swaps))
            return swaps

def minimumSwaps_v2(arr):
    narr=[x-1 for x in arr]
    ndict={x[0]:x[1] for x in enumerate(narr) if x[1]!=x[0]}
    
    while len(ndict.keys()>1):
        


    
 
print(minimumSwaps_v2([7,1,3,2,4,5,6]))
