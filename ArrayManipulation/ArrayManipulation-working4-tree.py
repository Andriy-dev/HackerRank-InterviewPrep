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
            
        def BTree_print(self):
            print("s>{} e>{} len>{} w>{}".format(self.start,self.end,self.length,self.weight))
            if self.left is not None:
                print("l>")
                self.left.BTree_print()
            if self.right is not None:
                print("r>")
                self.right.BTree_print()
        
        def insert(self,vector):
            # if __debug__:
            #     start=time()
            if self.start >= vector[0] and self.end <= vector[1]:
                self.weight+=vector[2]
                return
            if self.start > vector[1] or self.end < vector[0]: 
                # Nothing to see here
                return
            if self.left is None:
                # Creating left
                self.left=BTree(self.start,self.start + int((self.end - self.start)/2),0)
            if self.right is None:
                # Creatig right
                self.right=BTree(self.end - int((self.end - self.start)/2),self.end,0)
             
            self.left.insert(vector)  
            self.right.insert(vector)      
            # if __debug__ :
            #      print("Insert for {} completed in {}".format(vector,time()-start))
    
            
    def distance(n):
        #return(math.ceil(math.sqrt(n))**2-1)
        return(2**math.ceil(math.log(n,2)))
 
    tree=BTree(0,distance(n))
    
    # if __debug__:
    #     starttime=time()
    
    for query in sorted(queries,key=lambda x: x[0]):
        # if __debug__:
        #     starttime=time()  
        tree.insert([query[0]-1,query[1]-1,query[2]])
        # if __debug__:        
        #     print("Insert of {} completed in {}".format([query[0]-1,query[1]-1,query[2]],time()-starttime))
        
    # if __debug__:
    #     starttime=time()
    m=tree.max()
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
    
