import math
import sys
import time

class vEB():
    
    def __init__(self,u):
        self.k = math.ceil(math.log(u,2))
        self.u = 2**self.k
            
        self.most_significatnt = math.ceil(self.k/2)
        self.least_significant = math.floor(self.k/2)

        self.usr = 2**self.most_significatnt
        self.lsr = 2**self.least_significant
        
        self.cluster_size = self.usr # redundant assignemet, for readablity
        
        self.min = None
        self.max = None
        
        if __debug__:
            print("vEB class created. u={} self.u={} self.k={} self.most_significatnt={} self.least_significant={} self.usr={} self.lsr={}".format(u,self.u,self.k,self.most_significatnt,self.least_significant,self.usr,self.lsr))
        
        if self.u > 2:
            # no summary needed for self.u == 2; otherwise create summary
            if __debug__:
                print("Creating summary under {} size {}".format(self.u,self.usr))
            self.summary = vEB(self.usr)
            if __debug__:
                print("Creating cluster under {} size {} ".format(self.u,self.usr))
            self.cluster=[]
            for i in range(self.usr):
                self.cluster.append(vEB(self.usr))

        #else:
          #  if __debug__:
          #     print("Skipping summary and cluster creation, Base case u=2")
          #     self.summary = None
          #     self.cluster = None
            
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
        
    def vEBmin(self):
        return(self.min)
    
    def vEBmax(self):
        return(self.max)
    
    def vEBmember(self,x):
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            return(self.cluster[self.high(x)].vEBmember(self.low(x)))
            
    def vEBemptyinsert(self,x):
        self.min = x
        self.max = x
        
    def vEBinsert(self,x):
        if self.min is None :
            self.vEBemptyinsert(x)
        else:
            if x < self.min:
                # swap
                temp = self.min
                self.min = x
                x = temp
            if self.u > 2:
                if self.cluster[self.high(x)].vEBmin() == None:
                    if __debug__:
                        print("Inserting x={} self.high={} to summary".format(x,self.high(x)))
                    self.summary.vEBinsert(self.high(x))
                    if __debug__:
                        print("Executing vEBemptyinsert over v.cluster[self.high={}] self.low={}".format(self.high(x),self.low(x)))
                    self.cluster[self.high(x)].vEBemptyinsert(self.low(x))
                else:
                    if __debug__:
                        print("Executing vEBinsert over v.cluster[self.high={}] self.low={}".format(self.high(x),self.low(x)))
                    self.cluster[self.high(x)].vEBinsert(self.low(x))
            if x > self.max:
                self.max = x
            
if __name__ == '__main__':
    if len(sys.argv)==2:
        n=int(sys.argv[1])
    else:
        print("Usage : {} u ".format(sys.argv[0]))
        sys.exit()
    
    start=time.time()
    tree=vEB(n)
    print("Tree created for : {}".format(time.time()-start))
     
    x=100
    print("Insering {}".format(x))
    start=time.time()
    tree.vEBinsert(x)
    print("Speed per insertion: {}".format(time.time()-start))
     
    y=0
    start=time.time()
    print("Insering {}".format(y))
    print("Speed per insertion: {}".format(time.time()-start) )    
     
    tree.vEBinsert(y)
     
    print("min={} max={}".format(tree.min,tree.max))
        
     