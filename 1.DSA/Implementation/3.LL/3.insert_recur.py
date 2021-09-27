class Node:
    def __init__(self,data=0,next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def get_head(self):
        return self.head

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_all(self,arr):
        self.head = None
        for data in arr:
            self.insert_at_end(data)


def printll(head=None):
    itr = head
    while(itr):
        print(itr.data,end=', ')
        itr=itr.next

def insert_rec(head,data,pos):
    if(head==None or pos<0):
        return head

    if(pos==0):
        node = Node(data)
        node.next = head
        return node

    head.next = insert_rec(head.next,data,pos-1)   
    return head

ll = LinkedList()
ll.insert_all([1,2,3,4,5,6,7,8,9,10])
#printll(ll.get_head())
head = insert_rec(ll.get_head(),2,5)
printll(ll.get_head())
#head = insert_rec(head,2,1)
#head = insert_rec(head,2,2)
