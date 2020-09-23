from time import time
import math

def arrayManipulation(n, queries):
       
    def tinsert(tdict,vector):
        
            if tdict["sfw"][0]>= vector[0] and tdict["sfw"][1] <= vector[1]:
                tdict["sfw"][2]+=vector[2]
            elif not ( tdict["sfw"][0] > vector[1] or tdict["sfw"][1] < vector[0] ): 
                
                half_length = int((tdict["sfw"][1] - tdict["sfw"][0])/2)
                left_end = tdict["sfw"][0] + half_length
                right_start = tdict["sfw"][1] - half_length
                
                if vector[0] <= left_end or vector[1] <= left_end:
                    if "left" not in tdict :
                        tdict["left"]={"sfw":[tdict["sfw"][0],left_end,0]}
                    tinsert(tdict["left"],vector)
                    
                if vector[1] >= right_start or vector[1] >= right_start:  
                    if "right" not in tdict:
                        tdict["right"]={"sfw":[right_start,tdict["sfw"][1],0]}
                    tinsert(tdict["right"],vector)
 
    def tmax(tdict):
        if not ("left" in tdict):
            left = 0
        else:
            left = tmax(tdict["left"])

        if not ("right" in tdict):
            right = 0
        else:
            right = tmax(tdict["right"])
            
        return tdict["sfw"][2] + max(left,right)
            

    tdict={"sfw":[0,2**math.ceil(math.log(n,2)),0]}       #[0,n,0]} #[0,math.ceil(math.sqrt(n))**2-1,0]}
    
    # if __debug__:
    #     starttime=time()
        
    for query in sorted(queries,key=lambda x: x[1]):
        tinsert(tdict,[query[0]-1,query[1]-1,query[2]])
        
    # if __debug__:        
    #     print("Insert completed in {}".format(time()-starttime))
        
    # if __debug__:
    #     starttime=time()
        
    m=tmax(tdict)
    # if __debug__:        
    #     print("Max calculation completed in {}".format(time()-starttime))

    return(m)
    
if __name__=="__main__":
    
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
    
