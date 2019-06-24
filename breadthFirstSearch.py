# to note about dictionaries:
#   dictionaries can be indexed by keys, which can be any immutable type (string or numbers can always be keys)
#   Tuples can also be keys if they contain only strings, only numbers, or only tuples
#   lists cannot be used as keys since they are mutable
#   '{ }' creates an empty dictionary
#   use del to delete a key value pair
#   dict() can be used as a constructor 
#   dict comprehension:
#       {x: x**2 for x in (2, 4, 6)}
#       output: {2: 4, 4: 16, 6: 36}



# no proper data structure to create a graph in python but can use dictionaries
# f has no connecting nodes so it is by itself

# this is an undirected graph so it shows each node and what it is connected to
# the connections in an undirected graph are called edges
# the connections in a directed graph are called arcs

# this returns a list
def bfs(graph, start):
    if start not in graph.keys():
        return '{} is not a key'.format(start)
    explored = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

# adjacency list
graph = {"a" : ["c"],
         "b" : ["c", "e"],
         "c" : ["a", "b", "d", "e"],
         "d" : ["c"],
         "e" : ["c", "b"]
         # "f" : ["f"] # this means that this is an edge loop
}

# this is how to append a new key to a dictionary
#   graph.update({"g" : ["b"]})

# this is the only way i figured out how to update an existing list as a value in a dictionary
# if i did it like below then it will return none, since update overrides the existing value
#   temp = graph.get("a")
#   temp.append("d")

# can't do this will return none
#   some = [1, 2 ,3].append(4)


#graph.update({"a" : temp})

# this is a way to loop through the dictionary with its corresponding key and value
for k, v in graph.items():
    print(k, ': ',v)

# starting node is "a"


print(bfs(graph,"f"))


