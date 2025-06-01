# 🌟 Basic Idea of Red-Black Tree — Why It Was Introduced
**🚀 Goal:**
To keep a binary search tree (BST) balanced automatically, so that search, insert, and delete operations always take O(log n) time.

---
# 🧨 The Problem:
In a regular Binary Search Tree, if you insert nodes in sorted order (e.g. 1, 2, 3, 4, ...),
it becomes unbalanced, like this:
```
1
 \
  2
   \
    3
     \
      4
```
# ✅ The Solution: Self-Balancing Trees
Red-Black Tree was introduced to automatically balance the BST as you insert or delete nodes.

**It does this by:**

- Coloring nodes (Red or Black)

- Rotating parts of the tree

- Recoloring nodes

This keeps the tree height small and performance fast.

# 🤖 Why specifically Red-Black Trees?
**Because:**

- They're relatively simple to implement compared to other balanced trees (like AVL trees)

- Provide good enough balance

- Insertions and deletions are faster on average than in stricter trees like AVL

# 📌 Summary:
**Concept	Purpose:**

Red-Black Tree	-A self-balancing BST

Why introduced?	-To ensure fast (log n) operations

How?	-           Uses colors + rotations to stay balanced

Benefit	- Avoids worst-case slow BST performance

Sure! Here's a **basic and simple idea** of a **Red-Black Tree**:

---

### 🌳 What is a Red-Black Tree?

A **Red-Black Tree** is a type of **self-balancing binary search tree**.
It keeps the height of the tree **balanced**, so operations like **insert, delete, search** happen in **O(log n)** time.

---

### 🟥⬛ Key idea:

Each node is **colored** either **Red** or **Black** to help maintain balance.

---

### 📏 Red-Black Tree Rules (must always be true):

1. **Every node is either Red or Black**
2. **Root is always Black**
3. **No two red nodes in a row** (a red node can’t have a red child)
4. **Every path from a node to its leaves must have the same number of black nodes**
5. **New nodes are always inserted as Red** (then fixed)

---

### 🔧 Why these rules?

They **prevent the tree from becoming unbalanced**.
Even in the **worst case**, the height is **at most 2×log(n)**.

---

### 🔄 What happens when you insert or delete?

To maintain the rules, the tree may:

* **Recolor nodes**
* **Rotate** parts of the tree (left or right rotation)

These actions **rebalance** the tree automatically.

---

### 📦 Example:

Start with an empty tree, insert 10, 20, 30:

After fixing colors and rotating:

```
   20(B)
  /    \
10(R)  30(R)
```

Now the tree is balanced, and all rules are satisfied.

---

### 🧠 In summary:

Red-Black Tree =
**Binary Search Tree** + **Extra coloring rules** + **Rotations for balancing**

You get **fast and balanced** performance for all operations!

---
#  Basic structure of a Red-Black Tree node.
```python
class RedTree:
    def __init__(self, value):
        self.value = value          # Node value
        self.right = None           # Right child
        self.left = None            # Left child
        self.color = 'RED'          # New nodes are usually RED by default
        self.parent = None          # To help with rotations and fix-up
```

---

### 🔴 Simple Scenario: Inserting into a Red-Black Tree

We’ll insert: **10**, **20**, **30**

---

### Step 1: Insert 10

* Tree is empty → insert 10 as **root**
* New nodes are RED, but **root must be BLACK**

✅ So:

```
10 (Black)
```

---

### Step 2: Insert 20

* Insert 20 → it's RED (default)
* 20 is child of 10 (Black)

No violation (red child, black parent) → nothing to fix.

✅ Tree:

```
    10 (Black)
       \
       20 (Red)
```

---

### Step 3: Insert 30

* Insert 30 → it's RED
* Parent is 20 (Red) → now we have **two REDs in a row** ❌

### 🔧 Fix needed:

* 10 is Black (grandparent), 20 is Red (parent), 30 is Red (new)
* This is a **Right-Right (RR)** case → needs **Left Rotation** at 10

### ✅ After fixing:

* 20 becomes new root (Black)
* 10 and 30 become Red children

Final Tree:

```
     20 (Black)
    /     \
10 (Red) 30 (Red)
```

---

### 🎯 Summary of the insert steps:

1. Insert node as RED (default)
2. If parent is BLACK → no problem
3. If parent is RED → fix by:

   * Recoloring or
   * Rotating (Left or Right), depending on structure

---
# Insertion
```python
def insert(root,key):
    if root is None:
        node=RedTree(key)
        node.color="BLACK"
        return node
    if key < root.value:
        root.left = insert(root.left, key)
        root.left.parent=root
        violation(root.left)
    elif key > root.value:
        root.right = insert(root.right, key)
        root.right.parent=root
        violation(root.right)
    
    return root
```
Absolutely! Here's a **clear breakdown** of **when to recolor** and **when to rotate** in a **Red-Black Tree** after an **insertion**.

---

## ✅ WHEN TO **RECOLOR** vs **ROTATE** (insertion cases)

---

### ⚠️ Problem:

You inserted a new **RED node**, and now its **parent is also RED** → this breaks Red-Black Rule #3.

---

## 📌 CASES TO RECOLOR vs ROTATE:

| Case       | Situation                                                                           | Action                         | Why?                        |
| ---------- | ----------------------------------------------------------------------------------- | ------------------------------ | --------------------------- |
| **Case 1** | Parent = RED, Uncle = RED                                                           | ✅ **Recolor**                  | Push red up the tree        |
| **Case 2** | Parent = RED, Uncle = BLACK/None, inserted node is **Left-Left** or **Right-Right** | 🔄 **Rotate once** (LL or RR)  | Fix Red-Red, promote parent |
| **Case 3** | Parent = RED, Uncle = BLACK/None, inserted node is **Left-Right** or **Right-Left** | 🔁 **Rotate twice** (LR or RL) | Fix shape, then promote     |

---

## 🔄 CASE-BY-CASE EXAMPLES

---

### 🔴 **Case 1 – Recolor**

**When**:

* New node is RED
* Parent is RED
* Uncle is RED

**Do**:

* Recolor parent and uncle to **BLACK**
* Recolor grandparent to **RED**
* Repeat check at grandparent (it may cause new violation)

✅ This pushes the RED upward to rebalance.

---

### 🔁 **Case 2 – Rotate once (LL or RR)**

**When**:

* New node is RED
* Parent is RED
* Uncle is BLACK or None
* And it's a **straight line**:

  * Left child of Left child (**LL**)
  * Right child of Right child (**RR**)

**Do**:

* Rotate **once** at grandparent
* Recolor parent to BLACK and grandparent to RED

---

### 🔁 **Case 3 – Rotate twice (LR or RL)**

**When**:

* New node is RED
* Parent is RED
* Uncle is BLACK or None
* And it's a **zig-zag**:

  * Right child of Left child (**LR**)
  * Left child of Right child (**RL**)

**Do**:

* First rotate child → parent (e.g., Left Rotate at parent)
* Then rotate parent → grandparent (e.g., Right Rotate at grandparent)
* Recolor appropriately (new subtree root becomes BLACK)

---

## 🔧 Quick Visual Summary

| Pattern                          | Fix Action                      |
| -------------------------------- | ------------------------------- |
| RED parent + RED uncle           | Recolor (Case 1)                |
| RED parent + BLACK uncle + LL/RR | Rotate once + Recolor (Case 2)  |
| RED parent + BLACK uncle + LR/RL | Rotate twice + Recolor (Case 3) |

---


# Violation
```python
def violation(root):
    if root.parent is None or root.parent.color == "BLACK":
        return root

    parent = root.parent
    grandparent = parent.parent
    new_tree = None

    if grandparent is None:
        return root  # Avoids NoneType errors when there's no grandparent

    # Find uncle
    if grandparent.left == parent:
        uncle = grandparent.right
    else:
        uncle = grandparent.left

    # 🔴 Case 1: Red parent and red uncle → recolor
    if root.color == "RED" and parent.color == "RED" and uncle and uncle.color == "RED":
        parent.color = "BLACK"
        uncle.color = "BLACK"
        grandparent.color = "RED"
        return violation(grandparent)  # Recursively check upward

    # 🔁 Case 2/3: Red parent, black (or None) uncle → rotations
    if uncle is None or uncle.color == "BLACK":
        if grandparent.left == parent and parent.left == root:
            new_tree = LL(grandparent)  # Left-Left
        elif grandparent.right == parent and parent.right == root:
            new_tree = RR(grandparent)  # Right-Right
        elif grandparent.left == parent and parent.right == root:
            new_tree = LR(grandparent)  # Left-Right
        elif grandparent.right == parent and parent.left == root:
            new_tree = RL(grandparent)  # Right-Left

    # Recolor after rotation
    if new_tree:
        new_tree.color = "BLACK"
        if new_tree.left:
            new_tree.left.color = "RED"
            new_tree.left.parent = new_tree
        if new_tree.right:
            new_tree.right.color = "RED"
            new_tree.right.parent = new_tree

        # Connect to great-grandparent (if exists)
        new_tree.parent = grandparent.parent
        if grandparent.parent:
            if grandparent.parent.left == grandparent:
                grandparent.parent.left = new_tree
            else:
                grandparent.parent.right = new_tree

    return new_tree if new_tree else root
```

# Rotation
```python
def LL(grandparent):
    b = grandparent.left
    b1 = b.right

    b.right = grandparent
    grandparent.left = b1

    # Update parent pointers
    b.parent = grandparent.parent
    grandparent.parent = b
    if b1:
        b1.parent = grandparent

    return b

def RR(grandparent):
    b = grandparent.right
    b1 = b.left

    b.left = grandparent
    grandparent.right = b1

    # Update parent pointers
    b.parent = grandparent.parent
    grandparent.parent = b
    if b1:
        b1.parent = grandparent

    return b

def LR(grandparent):
    grandparent.left = RR(grandparent.left)
    grandparent.left.parent = grandparent  # Important to keep parent correct
    return LL(grandparent)

def RL(grandparent):
    grandparent.right = LL(grandparent.right)
    grandparent.right.parent = grandparent  # Important to keep parent correct
    return RR(grandparent)
```
