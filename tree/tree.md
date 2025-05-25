# 🌳 Tree Data Structure

A **Tree** is a non-linear data structure used to represent **hierarchical data**. It is used in applications like file systems, compilers, databases, artificial intelligence, and more.

---

## 🧠 Key Concepts

| Term        | Description |
|-------------|-------------|
| **Node**    | Each element in a tree. |
| **Root**    | The topmost node (only one root). |
| **Edge**    | A connection between two nodes. |
| **Child**   | A node that descends from another. |
| **Parent**  | A node that has children. |
| **Leaf**    | A node with no children. |
| **Subtree** | A tree formed from a node and its descendants. |

---

## 🧱 Example Tree Structure

```python
     A         <- Root
   /   \
  B     C      <- Children of A
 / \   / \
D   E F   G    <- Leaf nodes
```

- `A` is the root  
- `B`, `C` are children of `A`  
- `D`, `E`, `F`, `G` are **leaf nodes**  
- `B` is the **parent** of `D` and `E`  

---

## 📦 Types of Trees

| Tree Type             | Description |
|------------------------|-------------|
| **Binary Tree**        | Each node has at most 2 children. |
| **Binary Search Tree** | Left < Root < Right. |
| **AVL Tree**           | A self-balancing Binary Search Tree. |
| **Red-Black Tree**     | A height-balanced BST using red-black rules. |
| **Heap Tree**          | Used in priority queues (Min-Heap or Max-Heap). |
| **Trie**               | Used for efficient string/prefix searching. |
| **N-ary Tree**         | A node can have N children. |

---

## ✅ Applications

- 📁 File and folder structures  
- 🧠 Artificial Intelligence (game/decision trees)  
- 🗂️ Database indexing (B-Trees, B+ Trees)  
- 🌐 Network routing tables  
- 🧾 Compilers (abstract syntax trees)

---

# 🌳 Basic Definitions in Trees

Trees are a fundamental data structure used to represent hierarchical relationships. Below are essential terms and definitions to understand how trees work:

| Term                      | Definition |
|---------------------------|------------|
| **Node**                  | A basic unit of a tree that holds data. |
| **Root**                  | The topmost node of the tree. It has no parent. |
| **Parent**                | A node that has one or more child nodes. |
| **Child**                 | A node that descends from another node (its parent). |
| **Leaf (Terminal Node)**  | A node that has no children. |
| **Internal Node**         | A node that has at least one child (not a leaf). |
| **Edge**                  | A connection between two nodes (like a line). |
| **Path**                  | A sequence of nodes connected by edges. |
| **Ancestor**              | Any node on the path from a node to the root. |
| **Descendant**            | Any node that comes after a given node (down the tree). |
| **Subtree**               | A smaller tree formed from any node and its children. |
| **Sibling**               | Nodes that share the same parent. |
| **Degree of a Node**      | The number of children a node has. |
| **Degree of a Tree**      | The maximum degree among all nodes in the tree. |
| **Level**                 | The distance (in edges) from the root to a node. Root is level 0. |
| **Height of a Node**      | Number of edges on the longest path from that node to a leaf. |
| **Height of a Tree**      | Height of the root node (i.e., the longest path to a leaf). |
| **Depth of a Node**       | Number of edges from the root to that node. |
| **Balanced Tree**         | A tree where left and right subtrees of every node have similar heights. |
| **Binary Tree**           | A tree where each node has at most 2 children. |
| **Full Binary Tree**      | Every node has either 0 or 2 children. |
| **Perfect Binary Tree**   | All internal nodes have 2 children, and all leaves are at the same level. |
| **Complete Binary Tree**  | All levels are filled except possibly the last, which is filled from left to right. |
| **Skewed Tree**           | A tree where each node has only one child (left-skewed or right-skewed). |
| **Binary Search Tree (BST)** | A binary tree where left < node < right. Used for fast searching. |

---

# 🌳 Tree Terminology (Complete List)

Understanding tree terminology is crucial to mastering tree data structures. Below is a categorized list of terms with clear definitions.

---

## 🟢 1. Basic Components

| Term              | Description |
|-------------------|-------------|
| **Node**          | A unit in the tree that holds data and may connect to other nodes. |
| **Edge**          | A link/connection between a parent and a child node. |
| **Root**          | The topmost node in the tree (has no parent). |
| **Leaf (External Node)** | A node with no children. |
| **Internal Node** | A node that has at least one child. |
| **Null Node**     | A placeholder indicating no child in that direction (common in binary trees). |

---

## 🟢 2. Relationships

| Term        | Description |
|-------------|-------------|
| **Parent**  | A node that has one or more children. |
| **Child**   | A node that descends from another (the parent). |
| **Sibling** | Nodes with the same parent. |
| **Ancestor**| A node that comes before another node on the path to the root. |
| **Descendant** | A node that comes after another node (child, grandchild, etc.). |

---

## 🟢 3. Structural Concepts

| Term                  | Description |
|------------------------|-------------|
| **Subtree**            | A smaller tree formed from a node and its descendants. |
| **Degree of a Node**   | The number of children a node has. |
| **Degree of Tree**     | The maximum degree of any node in the tree. |
| **Path**               | A sequence of nodes connected by edges. |
| **Level**              | The distance from the root to the node (starting from 0). |
| **Depth of Node**      | Number of edges from the root to the node. |
| **Height of Node**     | Number of edges from the node to the deepest leaf. |
| **Height of Tree**     | Height of the root node (i.e., max height of all nodes). |
| **Balanced Tree**      | A tree where height difference between left and right subtree of every node is minimal. |
| **Skewed Tree**        | A tree where all nodes have only one child (left-skewed or right-skewed). |

---

## 🟢 4. Types of Trees

| Type                  | Description |
|------------------------|-------------|
| **Binary Tree**        | Each node has at most 2 children (left and right). |
| **Full Binary Tree**   | Every node has either 0 or 2 children. |
| **Perfect Binary Tree**| All internal nodes have 2 children and all leaves are at the same level. |
| **Complete Binary Tree** | All levels are full except possibly the last, which is filled from left to right. |
| **Degenerate Tree**    | A tree where each parent has only one child (behaves like a linked list). |
| **Balanced Binary Tree** | A binary tree where the height is minimized for fast access. |
| **Binary Search Tree (BST)** | A binary tree where left < node < right. |
| **AVL Tree**           | A self-balancing BST with height balance condition. |
| **Red-Black Tree**     | A balanced BST that uses colors to ensure balancing rules. |
| **N-ary Tree**         | A tree where a node can have N children (not limited to 2). |
| **Trie (Prefix Tree)** | A tree used for storing strings, especially for prefix searching. |
| **Heap Tree**          | A special complete binary tree used in heapsort and priority queues. |
| **B-Tree**             | A balanced tree used in databases and file systems. |

---

## 🟢 5. Tree Traversals

| Traversal Type          | Description |
|--------------------------|-------------|
| **Preorder**             | Visit root → left → right |
| **Inorder**              | Visit left → root → right |
| **Postorder**            | Visit left → right → root |
| **Level Order**          | Visit level by level (uses queue, also called BFS) |
| **Depth First Search (DFS)** | Uses preorder, inorder, or postorder logic |
| **Breadth First Search (BFS)** | Uses level order traversal logic |

---
