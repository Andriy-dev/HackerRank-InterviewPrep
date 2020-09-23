
class Vector:
        
        def __init__(self,x1,x2,weight):
            self.x1=x1
            self.x2=x2
            self.length=x2-x1
            self.weight=weight
    
        def intersect(self,y):
            if __debug__:
                print("Method intersect called with {} and {}".format(self,y))
    
            if not ( self.x2 >= y.x1 and y.x2 >= self.x1 ):
                # They are not intersecting
                return([self,Vector(0,0,0),y])
            else:
                # They are intersecting
                #
                # Intersecting on the left (with matching on the right)
                if (y.x1 <= self.x1 and y.x2 <= self.x2):
                    if __debug__:
                        print("*Left [{},{},{}] with [{},{},{}]".format(self.x1,self.x2,self.weight,y.x1,y.x2,y.weight))
                    if y.x1==self.x1:
                        segment1=Vector(0,0,0)
                    else:
                        segment1=Vector(y.x1,self.x1 - 1,y.weight)
                    
                    segment2=Vector(self.x1,y.x2,self.weight + y.weight)
                    if self.x2==y.x2:
                        segment3=Vector(0,0,0)
                    else:
                        segment3=Vector(y.x2 + 1,self.x2,self.weight)
                elif (y.x1 >= self.x1 and y.x2 >= self.x2):
                    if __debug__:
                        print("*Right [{},{},{}] with [{},{},{}]".format(self.x1,self.x2,self.weight,y.x1,y.x2,y.weight))
                    if y.x1==self.x1:
                        segment1=Vector(0,0,0)
                    else:
                        segment1=Vector(self.x1,y.x1 - 1,self.weight)
                    segment2=Vector(y.x1,self.x2,self.weight + y.weight)
                    if self.x2==y.x2:
                        segment3=Vector(0,0,0)
                    else:
                        segment3=Vector(self.x2 + 1,y.x2,y.weight)
                elif (self.x1 > y.x1 and self.x2 < y.x2):
                    if __debug__:
                        print("*inside ( y outside ) [{},{},{}] with [{},{},{}]".format(self.x1,self.x2,self.weight,y.x1,y.x2,y.weight))
                    segment1=Vector(y.x1,self.x1 - 1,y.weight)
                    segment2=Vector(self.x1,self.x2,self.weight + y.weight)
                    segment3=Vector(self.x2 + 1,y.x2,y.weight)
                elif (self.x1 < y.x1 and self.x2 > y.x2):
                    if __debug__:
                        print("*inside ( self outside ) [{},{},{}] with [{},{},{}]".format(self.x1,self.x2,self.weight,y.x1,y.x2,y.weight))
                    segment1=Vector(self.x1,y.x1 - 1,self.weight)
                    segment2=Vector(y.x1,y.x2,self.weight + y.weight)
                    segment3=Vector(y.x2 + 1,self.x2,self.weight)
                return([segment1,segment2,segment3])
            
        def __str__(self):
            return("Vector[{},{},{}]".format(self.x1,self.x2,self.weight))
            
        def __repr__(self):
            return("Vector[{},{},{}]".format(self.x1,self.x2,self.weight))   
            
        def __eq__(self,y):
            return (self.x1==y.x1 and self.x2==y.x2 and self.weight==y.weight)
        
if __name__ == '__main__':

    A=Vector(3,4,100)
    B=Vector(2,4,100)
    
    print(A)
    print(B)
    
    for n,v in enumerate(A.intersect(B)):
        print(n,v)    