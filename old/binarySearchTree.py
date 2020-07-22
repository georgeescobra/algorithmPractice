import random

class Node(object):
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.value < node.value: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)

#   assuming the array is unsorted
#   the left subtree should be a binary tree as well as the right subtree
#   right subtree/Node is larger than its parent
#   left subtree/Node is smaller than its parent

def arrayToBST(array):
    if not array:
        return None
    newArray = sorted(array)
    midPoint = len(newArray) // 2
    node = Node(newArray[midPoint])
    node.left = arrayToBST(newArray[:midPoint])
    node.right = arrayToBST(newArray[midPoint + 1:])
    return node

def preOrder(node): 
    if not node: 
        return      
    print(node.value)
    preOrder(node.left) 
    preOrder(node.right) 

unordered = [random.randint(0, 100) for i in range(50)]
result = arrayToBST(unordered)
preOrder(result)


