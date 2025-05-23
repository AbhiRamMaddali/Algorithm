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


from collections import deque

def bfs(graph, start):
    visit = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.add(node)
        if node in graph:  
            for neighbor in graph[node]:
                if neighbor not in visit:
                    queue.append(neighbor)
    return visit

graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 4],
    3: [0],
    4: [2]  
}
result = bfs(graph, 0)
print(result)  # Output: {0, 1, 2, 3, 4}

