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

Our DFS algorithm also works with such an approach. The first step is to set the two variables frontier and visited as below. Obviously, at the beginning of the frontier function, it will be equal to the initial node and the visited list will be empty.
```
frontier = [Node(self.init_state)]
visited = {}
```
The loop of our algorithm depends on the length of the frontier. The algorithm will continue until the length of this variable is greater than zero.
As mentioned, we have used the data stack structure in this algorithm. Therefore, in the first command, we pop the highest data of the stack. We put this popped data in a variable called node_1. Then we set the visit with the index of this state node equal to the node itself. Now everything is ready for successor to enter.

Before using the successor, we must check the equality of the desired state with the target state. In case of equality, the work of the function is finished and node is returned.

Now we have to set the actions. Actions are equal to the output of the successor function. As a result, all future statuses are placed in actions. In the next step, these actions are converted into acceptable nodes for the children of node_1 by the expand function. Finally, these children are added to the stack and the loop is resumed(In this store, we should avoid adding duplicate statuses).
```
    def dfs_search(self) -> Node:
        frontier = [Node(self.init_state)]
        visited = {}

        while len(frontier) > 0:  # Starting DFS loop
            node_1 = frontier.pop()
            visited[node_1.state] = node_1
            
            if State.is_goal(node_1.state, self.battlefield.points):
                return node_1
            
            actions = State.successor(
                node_1.state, self.battlefield
            )  # Add successors to frontier
            
            for child in node_1.expand(actions): 
                if child.state not in visited:
                    frontier.append(child)
```


https://stackoverflow.com/questions/5775352/python-return-2-ints-for-index-in-2d-lists-given-item

https://www.tutorialspoint.com/python/list_min.htm

https://stackoverflow.com/questions/10406130/check-if-something-is-not-in-a-list-in-python

https://stackoverflow.com/questions/8585897/why-does-indexof-return-1

https://stackoverflow.com/questions/34472814/use-a-any-or-a-all

https://www.geeksforgeeks.org/python-any-function/

https://www.geeksforgeeks.org/python-list-index/#:~:text=Python%20index()%20is%20an,index%20of%20the%20first%20occurrence.
