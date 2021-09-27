class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Trees:
    def __init__(self, root):
        self.root = Node(root)


    def preorder(self, root):
        if(root):
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


    def inorder(self,root):
        if(root):
            self.preorder(root.left)
            print(root.data, end=" ")
            self.preorder(root.right)


    def postorder(self, root):
        if(root):
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


    def preorder_iter(self, root):
        if(root):
            stk = []
            stk.append(root)

            itr = root
            while(stk):
                if itr:
                    print(itr.data, end=" ")
                    if itr.right:
                        stk.append(itr.right)
                    itr = itr.left
                else:
                    itr = stk.pop()
            

    def inorder_iter(self, root):
        if(root):
            stk = []

            itr = root
            while(stk or itr):
                if itr:
                    stk.append(itr)
                    itr = itr.left
                else:
                    itr = stk.pop()
                    print(itr.data, end=" ")
                    itr = itr.right
                    



    def postorder_iter(self, root):
        pass

