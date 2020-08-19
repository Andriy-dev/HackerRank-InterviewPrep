def sockMerchant(n, ar):
    print("sockMerchant called with param n=",n,"and ar=",ar)
    paired=[]
    a=0
    for sock in ar:
        print("sock=",sock)
        if sock in paired:
            paired.remove(sock)
            a+=1
        else:
			paired.append(sock)
    return a 

# def test_1():
#     array=[10,20,20,10,10,30,50,10,20]
#     assert sockMerchant(9,array) == 3

class TestClass:
    def test_one(self):
        array=[1,2,2,1,1,3,5,1,2]
        assert sockMerchant(9,array) == 3

    def test_two(self):
        array = [1,2,2,1,1,3,5,1,2]
        assert sockMerchant(9,array) == 4
