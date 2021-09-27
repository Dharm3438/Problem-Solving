class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None


    def print_ll(self):
        if(self.head==None):
            print('Linked List is Empty')
            return

        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + '-->' if itr.next else str(itr.data)
            itr = itr.next
        
        print(llstr)


    def get_len(self):
        ct = 0
        itr = self.head
        while itr:
            ct+=1
            itr = itr.next

        return ct


    def insert_beg(self, data):
        node = Node(data,self.head)
        self.head = node


    def insert_at(self,data,idx):
        if(idx<0 or idx>self.get_len()):
            raise Exception('Invalid Index')

        if(idx==0):
            self.insert_beg(data)
            return

        ct = 0
        itr = self.head
        while itr:
            if(ct==idx-1):
                node = Node(data,itr.next)
                itr.next = node
                break
            ct+=1
            itr = itr.next


    def insert_end(self,data):
        if(self.head==None):
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)


    def remove(self, data, idx):
        if(idx<0 or idx>self.get_len()):
            raise Exception('Invalid Index')

        if(idx==0):
            self.head = self.head.next
            return

        itr = self.head
        ct = 0
        while itr:
            if(ct==idx-1):
                itr.next = itr.next.next
                break
            ct+=1
            itr=itr.next


    def reverse(self):
        prev = None
        next = None
        itr = self.head
        while itr:
            next = itr.next
            itr.next = prev
            prev = itr
            itr = next
        self.head = prev
