class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

def printll(head):
    if head==None:
        return 

    itr = head
    while itr:
        print(itr.data, end=' ')

def get_len(head):
    itr = head
    ct = 0
    while itr:
        itr=itr.next
        ct+=1
    
    return ct

def insert_at_beg(head,data):
    node = Node(data)
    node.next = head
    head = node
    return head

def insert_at_end(head,data):
    node = Node(data)
    if(head==None):
        head = node
        return head
    
    itr = head
    while itr.next:
        itr=itr.next
        
    itr.next = node
    return head


def insert_at(head,data,pos):
    if(pos<0 or pos>get_len(head)):
        return head
    
    if pos==0:
        head = insert_at_beg(head,data)

    ct = 0
    itr = head
    while(itr):
        if ct==pos-1:
            node = Node(data)
            node.next = itr.next
            itr.next = node
            return head
        itr = itr.next
        ct+=1
    
    return head

def remove_at(head,data,pos):
    if(pos<0 or pos>get_len(head)):
        return head

    if pos==0:
        head = head.next
        return head

    ct = 0
    itr = head
    while itr:
        if ct==pos-1:
            itr.next = itr.next.next
            return head

        itr=itr.next
        ct+=1

    return head


    

    






