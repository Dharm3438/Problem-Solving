from typing import Container

class Toy:
    def __init__(self,toyId, toyBrand, toyType, price):
        self.toyId = toyId
        self.toyBrand = toyBrand
        self.toyType = toyType
        self.prcie = price


class ShowRoom:
    def __init__(self, toyList):
        if toyList is None:
            self.toyList = []
        else:
            self.toyList = toyList

    def updatePriceBasedOnBrandAndType(self, toyBrand, toyType, weightage):
        flg = 0
        for val in self.toyList:
            if(val.toyBrand == toyBrand and val.toyType == toyType):
                val.updatedPrice = self.price + self.price*weightage/100
            else:
                flg=1
        
        if(flg):
            return False
        else:
            return True

    def countToysByPrice(self,):
        avg_price = sum(self.toyList)/len(self.toyList)
        ct = 0
        for toys in self.toyList:
            if(toys.price>avg_price):
                ct+=1
        
        return ct

    
if __name__=='__main__':
    count=int(input())
    clist=[ ]
    for i in range(count):
        iid=int(input())
        l=int(input())
        b=int(input())
        h=int(input())
        p=int(input())
        c1=Container(iid,l,b,h,p)
        clist.append(c1)
    p1=(clist)
    inid=int(input())
    res1=p1.findcontainercost(inid)
    res2=p1.findmaxvolume()
    if(res1==None):
        print("No container found")
    else:
        print(res1)
    print(res2.id)
    print(res2.findVolume())