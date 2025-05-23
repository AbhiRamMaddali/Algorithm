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

```python
v = 5  # 5 vertices: 0 to 4

edges = [
    (1, 0, 1),
    (3, 0, 2),
    (1, 1, 2),
    (4, 1, 3),
    (2, 2, 3),
    (2, 3, 4),
    (5, 2, 4)
]

edges.sort()
parent = [i for i in range(v)]
rank = [0] * v

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

mst = []
total_weight = 0

for weight, u, v in edges:
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        mst.append((u, v, weight))
        total_weight += weight

print("Minimum Spanning Tree edges:", mst)
print("Total weight of MST:", total_weight)
```
```
OUTPUT
Minimum Spanning Tree edges: [(0, 1, 1), (1, 2, 1), (2, 3, 2), (3, 4, 2)]
Total weight of MST: 6

