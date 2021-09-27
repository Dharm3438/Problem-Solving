class Node:
    def __init__(self,data=0,next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def get_head(self):
        return self.head

    def get_len(self):
        itr = self.head
        ct = 0 
        while(itr):
            ct+=1
            itr = itr.next
        return ct

    def insert_beg(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_end(self,data):
        if(self.head==None):
            node = Node(data,self.head)
            self.head = node
        else:
            itr = self.head
            while(itr.next):
                itr = itr.next
            itr.next = Node(data)

    def insert_at(self,data,pos):
        if(pos==0):
            self.insert_beg(data)
        else:
            ct = 0
            itr = self.head
            while itr:
                if ct==pos-1:
                    node = Node(data,itr.next)
                    itr.next = node
                itr = itr.next
                ct = ct+1

    def insert_all(self,arr):
        self.head=None
        for data in arr:
            self.insert_end(data)

    def appendLastNFirst(self,n):
        len = self.get_len()
        val = len-n-1
        ct = 0
        itr = self.head
        itr2 = self.head
        while(itr2.next):
            itr2=itr2.next
    
        while(itr):
            if(val==ct):
                break
            itr = itr.next
            ct+=1

        tmp = self.head
        self.head = itr.next
        itr.next = None
        itr2.next = tmp

def printll(head):
    itr = head
    while(itr):
        print(itr.data, end=', ')
        itr=itr.next

ll = LinkedList()
ll.insert_all([1,2,3,4,5,6,7,8,9,10])
ll.appendLastNFirst(2)
printll(ll.get_head())





