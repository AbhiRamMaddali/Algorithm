class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Creating nodes
root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('F')
'''
        A
       / \
      B   C
     / \    \
    D   E    F
'''
