class Stack:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def push(self,data):
        self.arr.append(data)
        self.size+=1
    
    def pop(self):
        self.size-=1
        return self.arr.pop()

    def peek(self):
        return self.arr[-1]

    def is_empty(self):
        if(self.size==0):
            return True
        else:
            return False

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




