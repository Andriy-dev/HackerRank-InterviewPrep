from time import time
import math

def arrayManipulation(n, queries):

    # defining cluster size (can be manipulated)
    c = math.ceil(math.log(n,2))
    c = 5 # 10.478840112686157
    c = 10 # 10.992422103881836
    c = 100 # 40.32227802276611
    c = 2 # 11.395529985427856
    c = 3 # 9.586182117462158
    c = 4 # 9.40293002128601
    c = 3

    if __debug__:
        print("Cluster size {}".format(c))

    # defining universe (last level = (cluser_size)**(level))
    u = c**(math.ceil(math.log(n,c)))

    if __debug__:
        print("Universe size {}, input size {}".format(u,n))

    class ctree:

        def __init__(self,start,size,weight=0):
            self.weight=weight
            self.start=start
            self.end=start + size -1
            self.size=size
            self.cluster_size=int(self.size/c)
            self.cluster=[None]*c
            #if __debug__:
            #    print("Created ctree with self.weight={}, self.start={}, self.end={}".format(self.weight,self.start,self.end))

        def insert(self,vector):

            if vector[0] <= self.start and self.end <= vector[1]:
                #  vector[0] ... self.start ... self.end ... vector[1]
                self.weight+=vector[2]
                return

            if self.start > vector[1] or self.end < vector[0]: 
                # Nothing to see here
                #
                # vector[0]  ... vector[1] ... self.start
                # self.end   ... vector[0] ... vector[1]
                return

            # Vector fell under some clusters calling them one-by-one without optimization

            for i in range(c):
                if self.cluster[i] is None:
                    self.cluster[i]=ctree(self.start+self.cluster_size*i,self.cluster_size)
                self.cluster[i].insert(vector)

        def ctree_print(self):
            print("Ctree self.start={} self.end={} self.weight={}".format(self.start,self.end,self.weight))
            if self.cluster is not None:
                for cluster in self.cluster:
                    cluster.ctree_print()
            print("=== finished ctree self.start={} self.end={} self.weight={}".format(self.start,self.end,self.weight))

        def ctree_max(self):

            if self.size == 1:
                return self.weight
            else:
                return self.weight + max([x.ctree_max() for x in self.cluster if x is not None] + [0])


            if self.cluster is None:
                return self.weight
            else:
                return (self.weight + max([x.ctree_max() for x in self.cluster]))

    tree=ctree(0,u,0)
    
    if __debug__:
       starttime=time()
    
    for query in queries: #sorted(queries,key=lambda x: x[0]):
        #if __debug__:
        #    print("Inserting [{} {}] weight = {}".format(query[0]-1,query[1]-1,query[2]))
        tree.insert([query[0]-1,query[1]-1,query[2]])
        #if __debug__:
        #    tree.ctree_print()
    if __debug__:        
       print("Insert completed in {}".format(time()-starttime))
        
    if __debug__:
       starttime=time()
    m=tree.ctree_max()
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

    n=10
    queries=[[2,6,8],[3,5,7],[1,8,1],[5,9,15]]
    # expected 31
    print(arrayManipulation(n,queries))

    f = open("input07-q.txt")
    n,m=10000000,100000
    queries=[]
    for q in f:
        queries.append(list(map(int,q.split())))
    # expected 2497169732
    print(arrayManipulation(n, queries))
    
