
```python
import collections

def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])
    visited.add(root)  # Mark root as visited immediately

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited when enqueuing
                queue.append(neighbor)
    print(visited)

if __name__ == "__main__":
    graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}
    bfs(graph, 0)  # Output: {0, 1, 2, 3, 4}
```
