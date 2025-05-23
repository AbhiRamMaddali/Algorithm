
🌲 Prim's Algorithm – Minimum Spanning Tree (MST)
Prim’s Algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, weighted graph. It builds the MST incrementally by always choosing the edge with the smallest weight that connects a visited node to an unvisited node.

✅ Characteristics
Type: Undirected, Connected, Weighted Graph

Goal: Connect all nodes with minimum total edge weight, no cycles

Approach: Greedy

🧠 How It Works
Start from any node.

Add the smallest edge connecting the current MST to an unvisited node.

Repeat until all nodes are included in the MST.

⏱️ Time Complexity
Using Min Heap + Adjacency List: O(E log V)
where E = number of edges, V = number of vertices

``` python
import heapq

# Graph represented as an adjacency list
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

visited = set()
min_heap = []
result = []

# Start from node 0, with cost 0 and no parent (-1)
heapq.heappush(min_heap, (0, 0, -1))

while min_heap:
    weight, current_node, parent = heapq.heappop(min_heap)
    if current_node in visited:
        continue
    visited.add(current_node)

    if parent != -1:
        result.append((parent, current_node, weight))

    for neighbor, edge_weight in graph[current_node]:
        if neighbor not in visited:
            heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

# Print the Minimum Spanning Tree and its cost
print("Minimum Spanning Tree:")
total_weight = 0
for u, v, w in result:
    print(f"{u} - {v} : {w}")
    total_weight += w

print("Total cost of MST:", total_weight)
```
``` 
OUTPUT:

Minimum Spanning Tree:
0 - 1 : 2
1 - 2 : 3
1 - 4 : 5
0 - 3 : 6
Total cost of MST: 16

