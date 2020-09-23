import math

class BTree:
    def __init__(self,start,end,weight=0,left=None,right=None):
        self.start=start
        self.end=end
        self.length=end - self.start # +1
        self.weight=weight
        self.left=left
        self.right=right
        # if self.length > 0:
        #     self.left_start=self.start
        #     self.left_end=self.start + self.length/2
        #     self.right_start=self.lef_end + 1
        #     self.right_end=self.end
    
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
        if __debug__:
            print("Executing insert over {}".format(vector))
            print("Tree info:")
            self.BTree_print()
        if self.start >= vector[0] and self.end <= vector[1]:
            self.weight+=vector[2]
            return
        if self.start > vector[1] or self.end < vector[0]: 
            if __debug__:
                print("We are outside , stop processing {} > {} or {} < {}".format(self.start,vector[1],self.end,vector[0]))
            return
        if self.left is None:
            # Creating left
            self.left=BTree(self.start,self.start + int(self.length/2),0)
        if self.right is None:
            # Creatig right
            self.right=BTree(self.end - int(self.length/2),self.end,0)
         
        self.left.insert(vector)  
        self.right.insert(vector)      

def distance(n):
    return(math.ceil(math.sqrt(n))**2-1)
        
if __name__=="__main__":
    
    # queries=[[1, 5, 3],[4, 8, 7],[6, 9, 1]]
    # n=10
    # expected 10
    
    # #tree.BTree_print()
    
    # for query in queries:
    #     tree.insert(query)
    
    # #print("="*20)
    # #tree.BTree_print()
    
    # print(tree.max())
        
    f = open("input07-q.txt")
    n,m=10000000,100000
    
    tree=BTree(0,distance(n))
    
    queries=[]
    for q in f:
        queries.append(list(map(int,q.split())))

    for query in queries:
        tree.insert(query)
    
    #print("="*20)
    #tree.BTree_print()
    
    print(tree.max())
    
    
    