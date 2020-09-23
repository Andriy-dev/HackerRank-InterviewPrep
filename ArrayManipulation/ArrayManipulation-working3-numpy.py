from datetime import datetime
import numpy

def arrayManipulation(n, queries):
    # index, value
    a=numpy.asarray([0]*n)
    queries=numpy.asarray(queries)
    #squeries=sorted(queries,key=lambda x:x[0])
    # if __debug__:
    #     m=len(queries)
    #     c=0
        
    for (start_idx,end_idx,add_number) in queries:
        # if __debug__:
        #     start=datetime.now()
        start_idx-=1
        end_idx-=1
        # if __debug__:
        #     c+=1
        #     print("{} {}%".format(c,c*100/m))
        
        a=numpy.concatenate([a[:start_idx],(a[start_idx:end_idx + 1] + add_number),a[end_idx+1:]])

        # if __debug__:
        #     print("Completed in {} , with segment length = {}".format(datetime.now()-start,end_idx + 1 - start_idx))
    return max(a)
    
       
            
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
    
