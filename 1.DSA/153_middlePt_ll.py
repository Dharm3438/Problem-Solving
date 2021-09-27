# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None):
            return head
        
        itr = head
        ct = 0
        while(itr):
            ct+=1
            itr=itr.next
        
        slow=head
        fast=head
        
        while(fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
            
        if(ct%2==0):
            return slow.next
        else:
            return slow