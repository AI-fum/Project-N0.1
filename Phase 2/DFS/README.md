```
DFS(graph, start_node, end_node):
    frontier = new Stack()
    frontier.push(start_node)
    explored = new Set()
    while frontier is not empty:
        current_node = frontier.pop()
        if current_node in explored: continue
        if current_node == end_node: return success
        
        for neighbor in graph.get_neigbhors(current_node):
            frontier.push(neighbor)
        explored.add(current_node)
```
