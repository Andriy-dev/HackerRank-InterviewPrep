import math
import sys
import time

'''
This variant of vEB do not pre-provising tree in advance
'''

def arrayManipulation(n, queries):
    class vEB():
    
        def __init__(self,u,satellite_load=None):
            self.k = math.ceil(math.log(u,2))
            self.u = 2**self.k
                
            self.most_significatnt = math.ceil(self.k/2)
            self.least_significant = math.floor(self.k/2)
    
            self.usr = 2**self.most_significatnt
            self.lsr = 2**self.least_significant
            
            self.cluster_size = self.usr # redundant assignemet, for readablity
            
            self.min = None
            self.max = None
            
            # Attempt to introduce satellite data
            self.sattelite_load = satellite_load
            self.satellite_min  = satellite_load
            self.satellite_max  = satellite_load
            
            self.cluster = None
            self.summary = None
            
            
            # if self.u > 2:
            #     # no summary needed for self.u == 2; otherwise create summary
            #     if __debug__:
            #         print("Creating summary under {} size {}".format(self.u,self.usr))
            #     self.summary = vEB(self.usr)
            #     if __debug__:
            #         print("Creating cluster under {} size {} ".format(self.u,self.usr))
            #     self.cluster=[]
            #     for i in range(self.usr):
            #         self.cluster.append(vEB(self.usr))
    
            # else:
            #     if __debug__:
            #       print("Skipping summary and cluster creation, Base case u=2")
            #       self.summary = None
            #       self.cluster = None
                
        def high(self,x):
            # The function high(x) gives the most significant fits of x, producing the number of x's cluster.
            return(math.floor(x/self.lsr))
        
        def low(self,x):
            # The function low(x) gives the least significatn bits of x and provides x's position within its cluster
            return(x%self.lsr)
            
        def index(self,x,y):
            # The function index(x,y) builds an element number from x and y, treating x as the most significant
            # bits of the element nubmer from x and y as the least significant bits.  
            return(x*self.lsr + y)
        
        def vEBmember(self,x):
            if x == self.min or x == self.max:
                return True
            elif self.u == 2:
                return False
            else:
                return(self.cluster[self.high(x)].vEBmember(self.low(x)))
                
        def vEBemptyinsert(self,x,satellite_load=None):
            self.min = x
            self.max = x
            self.satellite_min = satellite_load
            self.satellite_max = satellite_load
            
        def vEBmin(self):
            return(self.min)
    
        def vEBmax(self):
            return(self.max)
            
        def vEBinsert(self,x,satellite_load = None):
            
            if self.cluster == None:
                if self.u > 2:
                    # no summary needed for self.u == 2; otherwise create summary
                    # if __debug__:
                    #     print("Creating summary under {} size {}".format(self.u,self.usr))
                    self.summary = vEB(self.usr)
                    # if __debug__:
                    #     print("Creating cluster under {} size {} ".format(self.u,self.usr))
                    self.cluster=[]
                    for i in range(self.usr):
                        self.cluster.append(vEB(self.usr,satellite_load))
            
            if self.min is None :
                self.vEBemptyinsert(x,satellite_load)
            else:
                if not ( satellite_load is None ):
                    if not ( self.max is  None ):
                        self.max+=satellite_load
                    else:
                        self.max=satellite_load
                if x < self.min:
                    # swap
                    temp = self.min
                    self.min = x
                    x = temp
                if self.u > 2:
                    if self.cluster[self.high(x)].vEBmin() == None:
                        # if __debug__:
                        #     print("Inserting x={} self.high={} to summary".format(x,self.high(x)))
                        self.summary.vEBinsert(self.high(x))
                        # if __debug__:
                        #     print("Executing vEBemptyinsert over v.cluster[self.high={}] self.low={}".format(self.high(x),self.low(x)))
                        self.cluster[self.high(x)].vEBemptyinsert(self.low(x),satellite_load)
                    else:
                        # if __debug__:
                        #     print("Executing vEBinsert over v.cluster[self.high={}] self.low={}".format(self.high(x),self.low(x)))
                        self.cluster[self.high(x)].vEBinsert(self.low(x),satellite_load)
                if x > self.max:
                    self.max = x
                
    tree=vEB(n,0)
    
    # if __debug__:
    #     starttime=time()
    
    for query in sorted(queries,key=lambda x: x[0]):
        # if __debug__:
        #     starttime=time()  
        for i in range(query[0] - 1, query[1] - 1):
            tree.vEBinsert(i,query[2])
        # if __debug__:        
        #     print("Insert of {} completed in {}".format([query[0]-1,query[1]-1,query[2]],time()-starttime))
        
    # if __debug__:
    #     starttime=time()
    m=tree.satellite_max
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
    
