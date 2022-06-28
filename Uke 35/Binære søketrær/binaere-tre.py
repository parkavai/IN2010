class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.element)
    
class treet:
    
    def insert(self, rotnode, x):
        if(rotnode == None):
            rotnode = Node(x)
        elif(x < rotnode.element):
            rotnode.left = self.insert(rotnode.left, x)
        elif(x > rotnode.element):
            rotnode.right = self.insert(rotnode.right, x)
        return rotnode
    
    def search(self, rotnode, x):
        if(rotnode == None):
            rotnode = Node(x)
        if(rotnode.element == x):
            return rotnode
        if(x < rotnode.element):
            return self.search(rotnode.left, x)
        if(x > rotnode.element):
            return self.search(rotnode.right, x)
    
    def FindMin(self, rotnode):
        if(rotnode.left == None):
            return rotnode
        else:
            return self.FindMin(rotnode.left)
    
    def skrivUt(self,rotnode):
        if(rotnode == None):
            return
        print(rotnode)
        self.skrivUt(rotnode.right)
        self.skrivUt(rotnode.left)
    
    def remove(self, rotnode, x):
        if(rotnode == None):
            return None
        if(x < rotnode.element):
            rotnode.left = self.remove(rotnode.left, x)
            return
        if(x > rotnode.element):
            rotnode.right = self.remove(rotnode.right, x)
            return
        if(rotnode.left == None):
            return rotnode.right
        if(rotnode.right == None):
            return rotnode.left
        u = self.FindMin(rotnode.right)
        rotnode.right = self.remove(rotnode.right, x)
        return rotnode


tre = treet()

node1 = Node(6)
node2 = Node(2)
node3 = Node(3)
node4 = Node(10)
node5 = Node(8)

tre.insert(node1, node2.element)
tre.insert(node1, node3.element)
tre.insert(node1, node4.element)
tre.insert(node1, node5.element)
print(tre.search(node1, node4.element))
print(tre.FindMin(node1))
tre.skrivUt(node1)




        
        
