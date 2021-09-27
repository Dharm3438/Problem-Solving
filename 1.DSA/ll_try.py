class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if(self.head==None):
            print('LinkedList is empty')

        itr = self.head
        while itr:
            print(itr.data, end=" ")
            itr=itr.next
        
        print()


    def get_len(self):
        ct = 0
        itr=self.head
        while itr:
            ct+=1
            itr=itr.next
        return ct


    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        if(self.head==None):
            self.head = Node(data, None)
            return

        itr = self.head
        while(itr.next):
            itr = itr.next

        itr.next = Node(data, None)   
    


    def insert_at(self, data, index):
        if(index<0 or index>self.get_len()):
            print('Invalid Index')
            return

        if(index==0):
            self.insert_at_beg(data)
            return

        ct = 0
        itr = self.head
        while itr:
            if ct==index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            ct+=1

    
    def remove_at(self, index):
        if(index<0 or index>self.get_len()):
            print('invalid index')
            return 
        
        if(index==0):
            self.head = self.head.next

        itr = self.head
        ct=0
        while itr:
            if(ct==index-1):
                itr.next = itr.next.next
                break
            itr = itr.next
            ct+=1

    def insert_values(self, data_lis):
        self.head = None
        for data in data_lis:
            self.insert_at_end(data)


if __name__=='__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at("blueberry",1)
    ll.remove_at(0)
    ll.print_ll()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print_ll()
    #ll.reverse()
    ll.insert_at_beg('jhbrhjg')
    ll.print_ll()
