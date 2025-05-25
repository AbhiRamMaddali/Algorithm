🔁 Tree Traversal Methods (Binary Tree)

🔹 Inorder (Left → Root → Right)
```python
  def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
```
---
🔹Preorder (Root → Left → Right)
```python
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
```
---
🔹 Postorder (Left → Right → Root)
```python
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
```
---
🔹 Level Order (Breadth-First)
```python
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```
---
🔹 Height or Depth of Binary Tree

✅ **1.Recursion**
```python
def height(root):
    if root is None:
        return -1  # we can write -1 or 0 depending on convention
    return 1 + max(height(root.left), height(root.right))
```
Recusion case
```
return 1 + max(height(root.left), height(root.right))
```
This means:

Find the height of the left subtree → height(root.left)

Find the height of the right subtree → height(root.right)

Take the maximum of those two heights

Add 1 to include the current node's edge to its child
```
         A
        / \
       B   C
      / \
     D   E
```
**Let's break it down:**

height(D) and height(E) return -1 for their left and right (since they're leaves).

height(D) = 1 + max(-1, -1) = 0

height(E) = 1 + max(-1, -1) = 0

height(B) = 1 + max(0, 0) = 1

height(C) = 1 + max(-1, -1) = 0

height(A) = 1 + max(1, 0) = 2

✅So the height of the tree is 2 (counting edges).

✅ 2. Iterative Approach
```python
from collections import deque

def height_iterative(root):
    if root is None:
        return -1  # Or 0, depending on whether you count height in edges or nodes

    queue = deque([root])
    height = -1

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        height += 1

    return height
```


