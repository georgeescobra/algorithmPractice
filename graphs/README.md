I am going to implement the various data structures for graph representation

1. Adjacency List
2. Adjacency Matrix
3. Incidence Matrix

G := graph
vertex := < x | y | z >
v: = value
Basic Operations:

1. adjacent(G, x, y)
2. neighbors(G, x)
3. add_vertex(G, x)
4. remove_vertex(G, x)
5. add_edge(G, x, y , z)
6. remove_edge(G, x, y)
7. get_vertex_value(G, x)
8. set_vertex_value(G, x, v)

Each kind of graph representation has different time and space complexities: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)#:~:text=Adjacency%20lists%20are,5%5D%5B6%5D

Best methods to traverse a graph:

1. BFS
2. DFS
