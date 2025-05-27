# 🌳 AVL Tree (Adelson-Velsky and Landis Tree)

## 📘 Definition
An **AVL Tree** is a self-balancing **Binary Search Tree (BST)** where the difference of heights between the left and right subtrees (called **Balance Factor**) of any node is at most **1**.

## 🔍 Why AVL Tree?
In a regular BST, insertion or deletion can cause the tree to become skewed, leading to **O(n)** time complexity for operations.

An AVL Tree maintains balance ⇒ ensures **O(log n)** time for insertion, deletion, and search.

## 🧠 Properties
- **Balance Factor (BF)** = Height of left subtree − Height of right subtree
- BF of any node must be **-1, 0, or +1**
- Height of AVL tree with n nodes is **O(log n)**

## 🔁 Rotations to Maintain Balance
When balance is disturbed after insertion or deletion, we perform rotations:

| Case               | Condition                      | Rotation       |
|--------------------|--------------------------------|----------------|
| Left-Left (LL)     | Insertion in left of left child | Right Rotate   |
| Right-Right (RR)   | Insertion in right of right child| Left Rotate    |
| Left-Right (LR)    | Insertion in right of left child | Left-Right    |
| Right-Left (RL)    | Insertion in left of right child | Right-Left    |

### ➖ Deletion Cases:
Similar to insertion, after deletion we check and fix balance using rotations.
# 🌳 AVL Tree Deletion – Complete Explanation

An **AVL Tree** is a self-balancing binary search tree where the **balance factor** (difference in height between left and right subtrees) of **every node** is **-1, 0, or +1**.

When we **delete a node** from an AVL Tree, we must ensure that the tree remains balanced.

---

## ✅ Deletion Steps in AVL Tree

### 1️⃣ Perform BST Deletion

Follow standard **Binary Search Tree (BST)** deletion logic:

- **No child** (leaf): Remove the node.
- **One child**: Replace the node with its child.
- **Two children**:
  - Find the **inorder successor** (smallest in right subtree).
  - Replace current node’s value with successor's value.
  - Recursively delete the successor.

---

### 2️⃣ Update Height

After deleting a node and returning back up the recursion stack, update the height of the current node:

```python
node.height = 1 + max(height(node.left), height(node.right))
```

## 🔧 Rotations Visual Example

**Right Rotation (LL):**
```
      z                              y
     / \                           /   \
    y   T4   =>    Right(z) =>    x     z
   / \                                 / \
  x   T3                             T3   T4
```
**Left Rotation (RR):**
```
    z                                 y
   / \                              /   \
  T1  y       =>     Left(z) =>    z     x
      / \                         / \
     T2  x                      T1   T2
```
---
**Right-Left (RL)– use Right Rotation + Left Rotation**
```
    z                                z                               x
   / \                             /   \                           /   \
  y   T4   →  Left(y) →          x    T4   →  Right(z) →         y      z
 / \                             / \                            / \    / \
T1  x                          y  T3                          T1 T2   T3 T4
    / \                       / \
  T2  T3                   T1  T2
```
**Left-Right (LR)– use Left Rotation + use Right Rotation**
```
      z                                z                               x
     / \                             /   \                           /   \
   T1   y      →   Right(y) →      T1    x     →   Left(z) →         z      y
       / \                           / \                            / \    / \
      x  T4                        T2  y                           T1 T2  T3 T4
     / \                               / \
   T2  T3                            T3  T4
```
---
**📈 Example:**
Insert 10 → 20 → 30 into an empty tree.

After inserting 30, the tree becomes unbalanced (Right-Right case).

Perform Left Rotation on node 10.

The tree becomes balanced again.
```
Before Rotation:         After Left Rotation:
     10                         20
       \                      /   \
       20       →           10    30
         \
         30
```

## 🛠️ AVL Tree Operations

1. **Insertion**  
   - Same as BST insertion.  
   - Update height.  
   - Check balance factor.  
   - Perform rotation if needed.

2. **Deletion**  
   - Same as BST deletion.  
   - Replace node if it has two children.  
   - Update height.  
   - Check and fix balance.

3. **Search**  
   - Same as BST, with **O(log n)** complexity.

---
**WHY AVL TREE**
---
# AVL Tree Explained Simply

## Imagine a Tree That Doesn’t Get "Lopsided"

A normal "family tree" (binary search tree) can get messy and tall on one side if you add or remove people randomly. This makes searching slow.

An **AVL tree** is a smart tree that **automatically fixes itself to stay balanced** — meaning no side gets too long or heavy.

---

## How Does It Stay Balanced?

Every person (node) in the tree checks their **Balance Factor** — the difference in height between their left and right sides.

**Example:**  
If Alice has 3 people on her left and only 1 on her right, that’s an imbalance. The left side is too heavy!

---

## Fix It with Rotations

If the tree becomes lopsided, it does simple rotations, like rearranging a shelf of books to spread them evenly:

- **Left-heavy?** Rotate right.  
- **Right-heavy?** Rotate left.  
- If it’s zig-zag shaped (left-right or right-left), do two rotations.

(Imagine grabbing a node and “twisting” the tree to spread it out evenly!)

---

## Why Care?

Because the tree is always balanced, operations like searching, inserting, and deleting are **fast and efficient** — guaranteed to work in **O(log n)** time.  
Unlike a messy normal tree that can become slow like a linked list, AVL trees stay quick.

---

## Real-Life Analogy

Think of an AVL tree like a **self-adjusting seesaw**. If one side gets heavier, it automatically shifts weights (rotations) to stay level.

---
## TL;DR:"Too Long; Didn't Read.

AVL trees are binary search trees that fix their own balance to stay short and efficient, using simple “twists” (rotations) whenever things get lopsided.

---
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if node is None:
        return 0
    return node.height

def get_balance(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

def right_rotate(A):
    B = A.left
    T3 = B.right

    B.right = A
    A.left = T3

    A.height = 1 + max(height(A.left), height(A.right))
    B.height = 1 + max(height(B.left), height(B.right))
    return B

def left_rotate(A):
    B = A.right
    T2 = B.left

    B.left = A
    A.right = T2

    A.height = 1 + max(height(A.left), height(A.right))
    B.height = 1 + max(height(B.left), height(B.right))
    return B

def insert(node, key):
    if not node:
        return Node(key)
    if key < node.value:
        node.left = insert(node.left, key)
    elif key > node.value:
        node.right = insert(node.right, key)
    else:
        return node  # Duplicate keys are not allowed

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    # LL
    if balance > 1 and key < node.left.value:
        return right_rotate(node)
    # RR
    if balance < -1 and key > node.right.value:
        return left_rotate(node)
    # LR
    if balance > 1 and key > node.left.value:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    # RL
    if balance < -1 and key < node.right.value:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

def deletion(node, key):
    if not node:
        return None

    if key < node.value:
        node.left = deletion(node.left, key)
    elif key > node.value:
        node.right = deletion(node.right, key)
    else:
        # Node to be deleted found
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        # Node with two children
        temp = node.right
        while temp.left:
            temp = temp.left
        node.value = temp.value
        node.right = deletion(node.right, temp.value)

    node.height = 1 + max(height(node.left), height(node.right))
    balance = get_balance(node)

    # LL
    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)
    # LR
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    # RR
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)
    # RL
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node
# Creating AVL Tree
node = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    node = insert(node, val)

print("Preorder Traversal Before Deletion:")
preorder(node)
print()

# Deleting node 50
node = deletion(node, 50)

print("Preorder Traversal After Deletion:")
preorder(node)
print()
```
**output**
```
Preorder Traversal Before Deletion:
50 30 20 40 70 60 80 
Preorder Traversal After Deletion:
60 30 20 40 70 80 


