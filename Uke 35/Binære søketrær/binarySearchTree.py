class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.element)
    
class BinarySearchTree:

    def __init__(self):
        self._root = None

    def insert(self, x):
        if(self._root == None):
            self._root = Node(x)
        else:
            self._root = self._recursiveInsert(x, self._root)
    
    def _recursiveInsert(self, x, node):
        if(node == None):
            node = Node(x)
        elif(x < node.element):
            node.left = self._recursiveInsert(x, node.left)
        elif(x >= node.element):
            node.right = self._recursiveInsert(x, node.right)
        return node 
    
    def search(self, x):
        if(self._root == None):
            print(self.error())
        else:
            node = self._recursiveSearch(self._root, x)
            if(node != None):
                print(f"Found the node with value '{node.element}' in BST")
            else:
                print(f"There wasn´t a node with value '{x}' in BST")
            return node

    def _recursiveSearch(self, node, x):
        if(node == None):
            return
        if(node.element == x):
            return node
        if(x < node.element):
            return self._recursiveSearch(node.left, x)
        if(x > node.element):
            return self._recursiveSearch(node.right, x)
    
    def findMin(self):
        if(self._root == None):
            print(self.error())
        else:
            lowest = self._recursiveFindMin(self._root)
            print(f"The lowest value in the BST is: {lowest}")
            return lowest
    
    def _recursiveFindMin(self, node):
        if(node.left == None):
            return node.element
        else:
            return self._recursiveFindMin(node.left)
    
    def findHigh(self):
        if(self._root == None):
            print(self.error())
        else:
            highest = self._recusiveFindHigh(self._root)
            print(f"The highest value in the BST is: {highest}")
            return highest
    
    def _recusiveFindHigh(self, node):
        if(node.right == None):
            return node.element
        else:
            return self._recusiveFindHigh(node.right)
    
    def writeOut(self,node):
        if(node == None):
            return
        print(node)
        self.writeOut(node.right)
        self.writeOut(node.left)
    
    def remove(self, x):
        if(self._root == None):
            print(self.error())
        else:
            removed = self._recursiveRemove(self, x, self._root)
            if(removed != None):
                print(f"Removed node with value'{removed.element}' from BST")
            else:
                print(f"There wasn´t a node with value '{x}' in BST to remove from")
            return removed

    def _recursiveRemove(self, node, x):
        if(node == None):
            return None
        if(x < node.element):
            node.left = self.remove(node.left, x)
            return node
        if(x > node.element):
            node.right = self.remove(node.right, x)
            return node
        if(node.left == None):
            return node.right
        if(node.right == None):
            return node.left
        u = self.FindMin(node.right)
        node.right = self.remove(node.right, u.element)
        return node

    def error(self):
        return "Root is null, assign a value to it!!!"

def testTree():
    bst = BinarySearchTree()

    # Insert nodes in BST
    bst.insert(50)
    bst.insert(40)
    bst.insert(60)
    bst.insert(20)
    bst.insert(56)
    bst.insert(4)

    # Test 1: Find the node with the lowest value
    if(bst.findMin() != "4"):
        print("Test 1: Correct, '4' is the lowest value \n")
    else:
        print("Test 1: Failed \n")
    
    # Test 2: Find the node with the highest value
    if(bst.findHigh() != "60"):
        print("Test 2: Correct, '60' is the value \n")
    else:
        print("Test 2: Failed \n")
    
    # Test 3: Search after node with value "20"
    if(bst.search(20).element != "20"):
        print("Test 3: Correct, found node with value '20' \n")
    else:
        print("Test 3: Failed \n")
    
testTree()

    




