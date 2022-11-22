## Depth First Search
Depth first search is dead simple. First, go to the specified start node. Now, arbitrarily pick one of that node’s neighbors and go there. If that node has neighbors, arbitrarily pick one of those and go there unless we’ve already seen that node. And we just repeat this process until one of two things happens. If reach the specified end node we terminate the algorithm and report success. If we reach a node with only neighbors we’ve already seen, or no neighbors at all, we go back one step and try one of the neighbors we didn’t try last time.

This algorithm is called depth first search because we always prioritize searching the deepest node we know about. If there are ties, they are broken arbitrarily, but once we break our first tie (picking which neighbor of the start node to explore first) we will not try to search the other neighbors of the start_node until the first neighbor (and all of its neighbors) have been fully explored.

Consider our maze, and a DFS implementation that breaks ties by searching up first, then right, then left, then right. Our algorithm will go straight up until it hits a wall, then straight to the right to arrive at our end node.

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
https://stackoverflow.com/questions/5775352/python-return-2-ints-for-index-in-2d-lists-given-item

https://www.tutorialspoint.com/python/list_min.htm

https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python

https://stackoverflow.com/questions/8585897/why-does-indexof-return-1

https://stackoverflow.com/questions/34472814/use-a-any-or-a-all

https://www.geeksforgeeks.org/python-any-function/
