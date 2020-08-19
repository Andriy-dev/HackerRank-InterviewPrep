from __future__ import print_function

def sortback(q):
    q1=[ [x,0] for x in q ]
    ideal=sorted(q)
    l = len(q)
    
    while True :
        isops=False
        for i in xrange(l-1):
            #print("Index {} {}".format(i,q1))
            if q1[i][0]>q1[i+1][0]: 
                #print("Trying to perform swap between {} and {} in {}".format(q1[i],q1[i+1],q1))
                if q1[i][1]>=2:
                    pass
                    #print("Cant perform swap between {} and {} in {} skipping...".format( q1[i],q1[i+1],q1))
                else:
                    #print("Checks are ok. Index {} Swapping between {} and {} in {}".format( i,q1[i],q1[i+1],q1))
                    tvalue=q1[i+1]
                    q1[i+1]=q1[i]
                    q1[i]=tvalue
                    q1[i+1][1]+=1
                    #print("Swapped.Now array looks like {}".format(q1))
                    isops=True
        if not isops:
            if [ x[0] for x in q1 ] != ideal:
                return "Too chaotic"
            else:
                return sum([x[1] for x in q1])
        


print(sortback([5,1,2,3,7,8,6,4]))