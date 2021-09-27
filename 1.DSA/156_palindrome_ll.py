def reverse(head_val):

    prev = None
    itr = head_val
    while(itr):
        nex = itr.next
        itr.next = prev
        prev = itr
        itr = nex

    return prev


def compareLists(head1, head2):
    tmp1 = head1
    tmp2 = head2
    while(tmp1 and tmp2):
        if(tmp1.data==tmp2.data):
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        else:
            return 0

    if(tmp1==None and tmp2==None):
        return 1

    return 0


def isPalindrome(head):
    slow_ptr = head
    fast_ptr = head
    prev = head

    minnode = None

    res = True

    if(head!=None and head.next!=None):
        while(fast_ptr!=None and fast_ptr.next!=None):
            fast_ptr=fast_ptr.next.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        if(fast_ptr!=None):
            minnode = slow_ptr
            slow_ptr = slow_ptr.next

        second_half = slow_ptr

        #making sure that first part ends
        prev.next=None

        second_half = reverse(second_half)

        res = compareLists(head, second_half)

        second_half = reverse(second_half)

        #if min node was present 
        if(minnode!=None):
            prev.next = minnode
            minnode.next = second_half
        else:
            prev.next = second_half

    return res