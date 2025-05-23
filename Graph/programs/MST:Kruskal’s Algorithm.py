🌉 Kruskal's Algorithm – Minimum Spanning Tree (MST)
Kruskal’s Algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, weighted graph.
It works by sorting all edges and picking the smallest edge that doesn't form a cycle using a Disjoint Set (Union-Find) structure.

✅ Characteristics
Type: Undirected, Connected, Weighted Graph

Goal: Connect all nodes with the minimum total edge weight, no cycles

Approach: Greedy (Edge-based)

🧠 How It Works
Sort all edges in non-decreasing order of weight.

Use Union-Find to check if adding an edge forms a cycle.

Add the edge if it connects two disjoint sets (i.e., no cycle).

Repeat until you include (V - 1) edges in the MST.

⏱️ Time Complexity
O(E log E) where E is the number of edges (for sorting)

Union-Find operations are almost constant time with path compression


