class Node:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size +=1

    def pop(self):
        if self.is_empty():
            return "Empty Err"
        tmp = self.head
        self.head= self.head.next
        self.size-=1
        return tmp.data

    def is_empty(self):
        if(self.size==0):
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return 'Empty Err'
        return self.head.data

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)

tmp1 = stack1.pop()
tmp2 = stack1.pop()
print(stack1.peek()) ##2
tmp3 = stack1.pop()
tmp3 = stack1.pop()
print(stack1.is_empty())
