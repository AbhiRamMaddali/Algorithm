Here we will study about graph 

| BASIC IDEA :  A graph is a fundamental data structure in computer science and mathematics used to model relationships between objects|
|--------------------------------------------------------------------------------------------------------------------------------------|

A graph consists of two main components:

Vertices (Nodes): Represent objects (e.g., people, cities, web pages).

Edges (Connections): Represent relationships or interactions between vertices (e.g., friendships, roads, hyperlinks).

-------------------------------------------------------Key Concepts of graph---------------------------------------------------------------

a. Directed vs. Undirected Graphs

Undirected Graph: Edges have no direction (e.g., Facebook friendships).

  ->Example: If Alice is friends with Bob, Bob is friends with Alice.

Directed Graph (Digraph): Edges have direction (e.g., Twitter follows).

  ->Example: Alice can follow Bob, but Bob might not follow Alice.

b. Weighted vs. Unweighted Graphs

  -->Weighted Graph: Edges have values (e.g., road distances, costs).

  -->Unweighted Graph: Edges have no values (just presence/absence).

c. Cycles

  Cycle: A path that starts and ends at the same vertex.

  Acyclic Graph: No cycles (e.g., family trees, dependency graphs).

### Table 3: Why Use Graphs?

Graphs model real-world systems with interconnected entities:

| **Application**             | **Vertices Represent** | **Edges Represent**                     |
|-----------------------------|------------------------|------------------------------------------|
| Social Networks             | Users                  | Friendships                              |
| Transportation Networks     | Cities                 | Roads or Flights                         |
| Web Pages (e.g., PageRank)  | Web Pages              | Hyperlinks                               |
| Task Dependencies           | Tasks                  | Dependencies (for scheduling and planning) |
