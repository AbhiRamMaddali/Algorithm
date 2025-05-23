# 📊 Graph Data Structures in Depth

Graphs are powerful tools for modeling real-world systems — from social networks to road maps. This guide covers the fundamentals, key concepts, and how to implement graphs in code. 🚀

---

## 🔹 1. What is a Graph?

A **graph** consists of two main components:

- **Vertices (Nodes)** 🟢: Represent objects  
  _Examples_: People, cities, web pages

- **Edges (Connections)** 🔗: Represent relationships  
  _Examples_: Friendships, roads, hyperlinks

---

## 🔸 2. Key Concepts

### a. Directed vs. Undirected Graphs

- **Undirected Graph** 🔄  
  - Edges have no direction  
  - _Example_: Facebook friendships  
    - If Alice is friends with Bob, then Bob is friends with Alice

- **Directed Graph (Digraph)** ➡️  
  - Edges have direction  
  - _Example_: Twitter follows  
    - Alice can follow Bob, but Bob might not follow Alice

---

### b. Weighted vs. Unweighted Graphs

- **Weighted Graph** ⚖️  
  - Edges have values like cost, distance, etc.  
  - _Example_: Road networks with distances

- **Unweighted Graph** 🪶  
  - Edges indicate presence/absence of connection only

---

### c. Cycles

- **Cycle** 🔁  
  - A path that starts and ends at the same vertex

- **Acyclic Graph** 🚫  
  - A graph with no cycles  
  - _Examples_: Family trees, dependency graphs

---

## 📌 3. Why Use Graphs?

Graphs are ideal for modeling interconnected data and complex relationships.

### Table 3: Applications of Graphs

| **Application**             | **Vertices Represent** | **Edges Represent**                     |
|-----------------------------|------------------------|------------------------------------------|
| 🧑 Social Networks           | Users                  | Friendships                              |
| 🛫 Transportation Networks   | Cities                 | Roads or Flights                         |
| 🌐 Web Pages (PageRank)      | Web Pages              | Hyperlinks                               |
| 📋 Task Dependencies         | Tasks                  | Dependencies (for scheduling)            |

---

## 📚 4. Basic Terminology

- **Degree** 📈  
  - Number of edges connected to a vertex

- **In-degree / Out-degree** ⬅️ ➡️  
  - In **directed graphs**, number of incoming and outgoing edges

- **Path** 🛣️  
  - A sequence of edges that connect two vertices

- **Connected Graph** 🔗  
  - A graph where there is a path between every pair of vertices

- **Subgraph** 🧩  
  - A smaller portion (subset) of a graph

---

## 💾 5. How Graphs Are Stored in Code

### a. Adjacency List ✅

Each vertex stores a list of its neighbors.

- **Space Complexity**: `O(V + E)`  
- **Efficient for**: Sparse graphs

  ```python
  graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
  } 

### b. Adjacency Matrix 🧮

A 2D array where matrix[i][j] = 1 indicates an edge from vertex i to j.

Space Complexity: O(V²)

Efficient for: Dense graphs

Example Matrix:

        A  B  C  D
    A   0  1  1  0
    B   1  0  0  1
    C   1  0  0  0
    D   0  1  0  0

## 🌟 6. Special Types of Graphs

### 🌳 Tree

- A **connected**, **acyclic**, **undirected** graph  
- Contains **no cycles**
- Has exactly **one less edge than vertices**  
  - Formula: `E = V - 1`

---

### 🟦🟥 Bipartite Graph

- Vertices can be **divided into two disjoint sets**
- **No edge** connects vertices **within the same set**
- All edges **connect a vertex from one set to the other**
- Commonly used in **matching problems** and **graph coloring**

---

### 🔄 Complete Graph

- Every vertex is connected to **every other vertex**
- **Highly dense** graph
- Total number of edges:  
  - **Undirected**: `V * (V - 1) / 2`  
  - **Directed**: `V * (V - 1)`

---

> 🧠 These special types are frequently asked in interviews and used in algorithm design, especially in problems involving trees, bipartite checks, and graph theory optimizations.

