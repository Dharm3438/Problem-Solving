"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        # Code here
        if(head==None or k==1):
            return head
            
        dummy = Node(0)
        dummy.next = head
        
        cur = dummy
        nex = dummy
        pre = dummy
        fl=0
        
        ct = 0
        while(cur.next != None):
            cur = cur.next
            ct+=1
            
        while(ct>=k):
            cur = pre.next
            nex = cur.next
            i=1
            while(i<k):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
                i+=1
            pre = cur
            ct-=k
            
            if(ct<k):
                fl = 1
                ct_tmp = ct
        
        if(fl):
            i=0
            while(i<ct_tmp):
                cur = pre.next
                nex = cur.next
                j=1
                while(j<ct_tmp):
                    cur.next = nex.next
                    nex.next = pre.next
                    pre.next = nex
                    nex = cur.next
                    j+=1
                pre = cur
                i += ct_tmp
                
        
        return dummy.next
#{ 
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends