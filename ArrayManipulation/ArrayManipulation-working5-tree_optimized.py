from time import time
import math

def arrayManipulation(n, queries):

    class BTree:
        def __init__(self,start,end,weight=0,left=None,right=None):
            self.start=start
            self.end=end
            #self.length=end - self.start  
            self.weight=weight
            self.left=left
            self.right=right

        
        def max(self):
            if self.left is None:
                left = 0
            else:
                left = self.left.max()
            if self.right is None:
                right = 0
            else: 
                right = self.right.max()
    
            return self.weight + max(left,right)
            
        def insert(self,vector):
            if self.start >= vector[0] and self.end <= vector[1]:
                self.weight+=vector[2]
                return
            if self.start > vector[1] or self.end < vector[0]: 
                # Nothing to see here
                return
            # Trying to optimize
            half_length = int((self.end - self.start)/2)
            left_end = self.start + half_length
            right_start = self.end - half_length
            
            if vector[0] <= left_end or vector[1] <= left_end:
                if self.left is None:
                    # Creating left
                    self.left=BTree(self.start, left_end,0)
                self.left.insert(vector)
                
            if vector[0] >= right_start or vector[1] >= right_start:
                if self.right is None:
                    # Creating right
                    self.right=BTree(right_start, self.end, 0)
                self.right.insert(vector)    
    
    def distance(n):
        #return(math.ceil(math.sqrt(n))**2-1)
        return(2**math.ceil(math.log(n,2)))
        
    tree=BTree(0,distance(n))
    
    if __debug__:
        starttime=time()
        
    for query in queries: #sorted(queries,key=lambda x: x[0]):
        tree.insert([query[0]-1,query[1]-1,query[2]])
    if __debug__:        
        print("Insert completed in {}".format(time()-starttime))
        
    if __debug__:
        starttime=time()
    m=tree.max()
    if __debug__:        
        print("Max calculation completed in {}".format(time()-starttime))

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
    
