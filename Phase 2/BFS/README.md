## BFS

BFS is a graph traversal algorithm which starts at the root node and searches the graph layer by layer. It is an uninformed search algorithm and uses FIFO structure. All nodes in this algorithm are either visited or not visited. BFS starts at the root node and adds it to a queue. While the queue is not empty, it visits the first node and removes it from the queue. Then it adds the node to visited nodes and its adjacent nodes to the queue. Next it goes to the node’s next adjacent node that is not visited. It continues visiting adjacent nodes layer by layer until we reach the goal node or the queue is empty. 

We define a queue and add the Init_state which is our initial state to it. The queue contains all the nodes that are not visited and we can visit next. Then we initialise the vis variable which keeps the visited nodes in it. 

```
    queue = [Node(init_state)]
    vis = {}  # visited nodes
```
We declare that while the length of the queue is larger than zero, or in other words, the queue is not empty do the following tasks. The queue follows the FIFO principle so it removes the first node of the queue and marks it as visited. 
Then we check if the current_node is the goal state. If it’s the goal state we return the current node, otherwise we continue into the loop.

```
   while len(queue) > 0:  # Starting BFS loop
        current_node = queue.pop(0)
        vis[current_node.state] = current_node

        if State.is_goal(current_node.state, self.battlefield.points):
            return current_node
```
We find current_node’s adjacent neighbours with the successor function and keep it in actions variable. Then we convert actions to nodes with the expand function and add them to the queue to be visited.