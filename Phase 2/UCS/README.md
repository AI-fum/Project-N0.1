## UCS

UCS is an uninformed search algorithm on a weighted graph which goes from the start node to the goal node with the minimum cumulative cost. 
We define a variable heap from the class MinHeap. This variable keeps the next nodes we can go from the current node. The visited variable is a set that contains the visited nodes. source_node is the start node and contains init_state in it. The first element of heap is source node.

```
    heap = MinHeap()
    visited = set()
    source_node = Node(self.init_state)
    heap.add(source_node)
```
This algorithm works in a way that while the heap is not empty, store the smallest element of heap which has the least cumulative cost in the node variable. If the state is goal, the node is returned otherwise it continues into the loop. If the node isn’t in the visited set, it is added to it otherwise it continues from the beginning of the loop. 
The next states are stored in the actions variable. The for loop converts actions to nodes with the expand function and adds them to the heap to be visited next.

```
    while not heap.is_empty():
        node = heap.pop()

        if State.is_goal(node.state, self.battlefield.points):
            return node

        if node.state not in visited:
            visited.add(node.state)
        else:
            continue

        actions = State.successor(node.state, self.battlefield)
        for child in node.expand(actions):
            heap.add(child)
```
