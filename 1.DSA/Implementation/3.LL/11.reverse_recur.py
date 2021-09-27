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
    
    def reve_recur(self,head):
        if(head==None or head.next==None):
            return head
        smallans = self.reve_recur(head.next)
        tmp = smallans
        while tmp.next!=None:
            tmp = tmp.next
        tmp.next = head
        head.next = None
        return smallans


def printll(head):
    itr = head
    while(itr):
        print(itr.data, end=', ')
        itr=itr.next
    print()

l1 = LinkedList()
l1.insert_all([30,22,20,5,1])
l2 = LinkedList()
l2.insert_all([2,3,6,11])
#printll(merge_ll(l1.get_head(),l2.get_head()))
#printll(merge_sort(l1.get_head()))
printll(l1.reve_recur(l1.get_head()))