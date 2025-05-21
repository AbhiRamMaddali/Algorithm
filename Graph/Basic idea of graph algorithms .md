# 🌐 Common Graph Algorithms — Simple Breakdown

Graphs are everywhere, and these algorithms help us **understand, explore, and optimize** them.

---

## 🌟 1. Graph Traversal  
**Goal:** Visit all nodes in a graph.

- **Breadth-First Search (BFS)**  
  - Explore nodes **layer by layer** (like ripples in water)  
  - Uses a **queue**  
  - **Use Case:** Shortest path in unweighted graphs, friends-of-friends

- **Depth-First Search (DFS)**  
  - Explore as **deep as possible** before backtracking  
  - Uses a **stack** or recursion  
  - **Use Case:** Maze solving, path existence checking

---

## 🚀 2. Shortest Path  
**Goal:** Find the quickest/cheapest route between nodes.

- **Dijkstra’s Algorithm**  
  - "Greedily" picks the closest node first  
  - Works only with **non-negative weights**  
  - **Use Case:** GPS navigation, network routing

- **Bellman-Ford Algorithm**  
  - Relax all edges repeatedly  
  - Handles **negative weights**  
  - **Use Case:** Detecting negative cycles (e.g., arbitrage)

- **Floyd-Warshall Algorithm**  
  - Compares **all possible paths** between every pair of nodes  
  - **Use Case:** Precomputing shortest paths (e.g., Google Maps)

---

## 🌳 3. Minimum Spanning Tree (MST)  
**Goal:** Connect all nodes with **minimum total cost** (no cycles).

- **Kruskal’s Algorithm**  
  - Sort edges by weight, add smallest edges avoiding cycles  
  - **Use Case:** Building cost-efficient road networks

- **Prim’s Algorithm**  
  - Grow MST from a starting node, always adding cheapest edge  
  - **Use Case:** Efficient wiring of electrical grids

---

## 🔗 4. Connectivity  
**Goal:** Identify connected components or groups.

- **Union-Find (Disjoint Set)**  
  - Group nodes into sets, merge when connected  
  - **Use Case:** Social network friend groups, Kruskal’s MST

- **Tarjan’s / Kosaraju’s Algorithm**  
  - Find strongly connected components in directed graphs  
  - **Use Case:** Web clusters, recommendation systems

---

## 🌊 5. Flow Networks  
**Goal:** Maximize flow (e.g., water, data) through a network.

- **Ford-Fulkerson Algorithm**  
  - Push flow through paths, reverse flow to optimize  
  - **Use Case:** Traffic optimization, plumbing systems

- **Edmonds-Karp Algorithm**  
  - Uses BFS to find shortest augmenting path in Ford-Fulkerson  
  - **Use Case:** Faster max-flow calculations

---

## 📂 6. Topological Sorting  
**Goal:** Order nodes so all dependencies come first.

- **Kahn’s Algorithm**  
  - Repeatedly remove nodes with no incoming edges  
  - **Use Case:** Course scheduling, build systems (like `make`)

---

## 🌀 7. Eulerian & Hamiltonian Paths

- **Eulerian Path (Hierholzer’s Algorithm)**  
  - Traverse every edge exactly once  
  - **Use Case:** DNA sequencing, garbage routes

- **Hamiltonian Path**  
  - Visit every node exactly once  
  - **Use Case:** Traveling Salesman Problem, circuit design

---

## 🎨 8. Graph Coloring  
**Goal:** Color nodes so no two neighbors share the same color.

- **Greedy Coloring**  
  - Color nodes one-by-one using smallest available color  
  - **Use Case:** Timetable scheduling, compiler register allocation

---

## 🤖 9. PageRank (Google’s Algorithm)  
**Basic Idea:** Measure node importance based on "votes" (links).

- **Use Case:** Ranking web pages in search results

---

## 🧩 Why This Matters

Graph algorithms power:

- **Social media** (friend suggestions)  
- **Google Maps** (shortest routes)  
- **Amazon** (recommendations)  
- **Internet** (data packet routing)

Each algorithm solves unique problems by cleverly exploring connections!

---

Feel free to ask if you'd like me to add **code samples**, **visual diagrams**, or explanations for any specific algorithm! 😊
