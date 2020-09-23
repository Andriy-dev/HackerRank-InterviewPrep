import math

class BTree:
    def __init__(self,start,length,weight=0,left=None,right=None):
        self.start=start
        self.length=length
        self.end=self.start + self.length
        self.weight=weight
        self.left=left
        self.right=right
    
    def str(self):
        return("w={} s={} e={} l={}".format(self.weight,self.start,self.end,self.length))
    
    def max(self):
        return self.weight + max(self.left,self.right)
        
    def BTree_print(self):
        if self.right is not None:
        print(self.weight)
        print("l>")
        self.left.BTree_print()
        print("r>")
        self.right.BTree_print()

def distance(n):
    return(math.ceil(math.sqrt(n))**2-1)
        
if __name__=="__main__":
    
    queries=[[1, 5, 3],[4, 8, 7],[6, 9, 1]]
    n=10
    # expected 10
    
    tree=BTree(0,distance(n))
    tree.BTree_print()
    
    
    
    