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

