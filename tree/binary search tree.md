# 🌳 Binary Search Tree (BST) – Basic Idea & Overview

---

## 📘 What is a Binary Search Tree?

A **Binary Search Tree (BST)** is a type of binary tree that maintains elements in **sorted order**, making it efficient for:

- 🔍 Searching
- ➕ Insertion
- ❌ Deletion

### 🧱 BST Rules:
- Each node has **at most two children**: left and right.
- **Left child** < parent node.
- **Right child** > parent node.

---

## 🧠 Key Properties

- 📌 **No Duplicates** (usually): All elements are unique.
- 🧭 **Inorder Traversal** gives sorted data.
- 🔁 **Recursive Structure**: Every subtree is a BST.

---

## 🔍 Example: Insert these values in order
50, 30, 70, 20, 40, 60, 80
```
        50
       /  \
     30    70
    / \    / \
  20  40  60  80
```

# ⚙️ BST Operations
1️⃣ Search
- Start at root.

- If value < node → go left.

- If value > node → go right.

- Repeat until found or reach a leaf.

2️⃣ Insert
- Use the same logic as search.

- Insert new node where None is reached.

3️⃣ Delete
Handle 3 cases:

- Leaf node → remove directly.

- One child → replace node with its child.

- Two children → replace with inorder successor or inorder predecessor.

# ⏱️ Time Complexity
Operation	Best / Avg Case	Worst Case (Unbalanced Tree)
- Search → O(log n)	O(n)
- Insert → O(log n)	O(n)
- Delete → O(log n)	O(n)

⚠️ If not balanced, a BST can degrade into a linked list.

💡 Real-World Use Cases
# 📚 Database indexing

- 🔍 Auto-complete suggestion systems

- 📂 File systems

- 🌐 Representing hierarchical data
---
# Understanding why BST

---

### 🧠 **Basic Idea of a Binary Search Tree (BST) – Why It Was Introduced**

#### ✅ **Purpose**:

The **Binary Search Tree** was introduced to make **searching**, **inserting**, and **deleting** data more efficient than linear structures like arrays or linked lists.

---

### 💭 **The Problem with Linear Structures (like arrays/lists):**

Imagine you have a list of numbers:

```
[4, 10, 2, 15, 6]
```

If you want to find if `15` exists:

* In a normal list, you might have to check **each element one by one** (linear search) → **O(n)** time.

---

### ✅ **The Solution: A Tree That Follows Binary Search Rules**

A **BST** is designed so that:

* At each step, you can eliminate **half of the elements** — just like **binary search** on a sorted array.
* This reduces the time complexity to **O(log n)** in the best and average cases.

---

### ⚙️ **How It Helps**

If the tree is **balanced**, operations are much faster:

* ✅ **Search** → log(n)
* ✅ **Insert** → log(n)
* ✅ **Delete** → log(n)

It’s like having a phone book where:

* You don’t read every name to find “Raj”
* Instead, you open near “R”, skip half, then half again, and find it quickly.

---

### 📌 **In Short**

> **Binary Search Trees were introduced to organize data in a way that makes search and update operations much faster than linear structures.**

---
#  INSERTION OF BST
```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.value:
        root.left = insert(root.left, key)
    elif key > root.value:
        root.right = insert(root.right, key)
    return root
```
# ✅ BST Search Function
```python

def search(root, key):
    if root is None or root.value == key:
        return root
    if key < root.value:
        return search(root.left, key)
    else:
        return search(root.right, key)
```

# 🔍 How it works:
- Base case: If root is None or root.value == key, it returns the current node (or None if not found).

Recursive step:

- If key < root.value, search the left subtree.

- If key > root.value, search the right subtree.
# 🔁 Iterative BST Search
```python
def search(root, key):
    while root is not None:
        if key == root.value:
            return root
        elif key < root.value:
            root = root.left
        else:
            root = root.right
    return None
```
# BST Deletion
```python
def deletion(node, key):
    if node is None:
        return None
    if key < node.value:
        node.left = deletion(node.left, key)
    elif key > node.value:
        node.right = deletion(node.right, key)
    else:
        # Node with only one child or no child
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        # Node with two children: get the inorder successor (min in right subtree)
        temp = node.right
        while temp.left:
            temp = temp.left
        node.value = temp.value
        node.right = deletion(node.right, temp.value)
    return node
```
# 🔥 Goal:
Remove a node with a given key from a Binary Search Tree while keeping the BST properties intact.
---
# 🧠 How it works (Step-by-step):
1. Find the node to delete:
- If key < node.value: go left

- If key > node.value: go right

- If key == node.value: this is the node to delete
---
# 🔄 Now 3 possible cases:
✅ Case 1: Node has no children (leaf node)
→ Just remove it (return None)

✅ Case 2: Node has 1 child
→ Return the child to replace the node

✅ Case 3: Node has 2 children
→ Find the smallest value in the right subtree (called the inorder successor), replace current node’s value with it, and delete that successor node from the right subtree

