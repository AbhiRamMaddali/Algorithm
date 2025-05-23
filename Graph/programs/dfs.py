#iterative
def dfs(graph,start):
  visit=set()
  stack = [start]
  while stack:
     node =stack.pop()
     if node not in visit:
        print(node)
        visit.add(node)
        # reversed is used :Reverse to maintain DFS order (LIFO)
     for n in reversed(graph[node]):
         if n not in visit:
          stack.append(n)
  
       
graph={'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]}
dfs(graph, 'A') #output: A,B,E,C,D

# recursion
graph={'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]}
visited=set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A') #output: A,B,E,C,D
