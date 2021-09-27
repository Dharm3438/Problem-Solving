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
        ct = 0
        itr = self.head
        while(itr):
            ct+=1
            itr= itr.next
        return ct

    def insert_beg(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_end(self,data):
        if(self.head==None):
            node = Node(data)
            self.head = node
        else:
            itr = self.head
            while(itr.next):
                itr = itr.next
            itr.next = Node(data)

    def insert_at(self,data,pos):
        if(pos==0):
            self.insert_beg(data)
            return
        ct = 0
        itr = self.head
        while(itr):
            if ct==pos-1:
                node = Node(data,itr.next)
                itr.next = node
            itr = itr.next
            ct+=1

    def insert_all(self,arr):
        self.head=None
        for data in arr:
            self.insert_end(data)

def printll(head):
    itr = head
    while(itr):
        print(itr.data,end=', ')
        itr = itr.next
    print()

def remove_recur(head,pos):
    if(head==None):
        return head

    if(pos==0):
        head=head.next
        return head

    head.next = remove_recur(head.next,pos-1)
    return head

ll = LinkedList()
ll.insert_all([1,2,3,4,5,6,7,8,9,10])
remove_recur(ll.get_head(),3)
printll(ll.get_head())
