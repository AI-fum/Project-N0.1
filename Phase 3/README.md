## A*
Acorrdig to wikipedia A* (pronounced "A-star") is a graph traversal and path search algorithm, which is used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches; however, A* is still the best solution in many cases.

<p align="center">
<img src="https://s6.uupload.ir/files/screencast_from_22-12-09_10_14_28_gb5i.gif" alt="This will display an animated GIF" >
</p>

In this program, we use Manhattan distance as the main function. So, to implement h, we need the main body of this function. In the next step, we can implement sigma on this function. The general form of this function to find the distance between two points in the Cartesian coordinate plane will be as follows.
```
        def manhattan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
            d1 = point1[0] - point2[0]
            d2 = point1[1] - point2[1]
            if d1 < 0:
                d1 = d1*(-1)
            if d2 < 0:
                d2 = d2*(-1)
                
            manhattan_distance = d1 + d2
            return manhattan_distance
```

Now we are using the Manhattan distance to implement the heuristic function. For this, we first receive a state as an input. Then we define a variable to calculate the sum of the distances. Initially, this variable is equal to zero. In the next step, the loop starts working. For each butter, the minimum value of the distance to the point is set to infinity. Then the distance of each butter to the point is checked and if it is minimum, it is placed in the mentioned variable. Finally, all these minimum distances are added together and placed in the variable related to the total distance.

With the help of this function, the robot can check how close it is to the points. This is our trump card in this algorithm. We implement this function as follows.
```
        def heuristic(state: State) -> int:
            total_distance = 0
            for butter in state.butters:
                min_distance = float("inf")
                for point in self.battlefield.points:
                    curr_distance = manhattan_distance(point, butter)
                    if curr_distance < min_distance:
                        min_distance = curr_distance
                total_distance += min_distance

            return total_distance
```
In next step, we must call the heuristic function for each node. Before starting *A process, it is better to talk about MinHeap. Hash Function is a one-way function that should preferably be one-to-one; It means that for every x there is only one y. In general, we do not have a limit for hash functions. For this function we need to design a heap type data structure. In this data structure we will have the following functions. Due to the large amount of content in this section, we refrain from fully explaining these functions and will limit ourselves to introducing them.

- make
- add
- remove
- modify
- pop
- is_empty
- value_of
- get_vertex
- min_heapify
- min_up_heapify
- right
- left
- parent
- swap
- minimum
- print

After introducing these functions, we will start working on the main algorithm. To do this, in the first step, we put the initial state as the root of the heap. For this, we set the root variable equal to the initial state and add it to the heap. This is where the algorithm loop starts. The loop of this algorithm will continue until the heap is empty. In the first step, a data is popped from the heap in a metric named node. Then the algorithm checks the point of this state. If this state is equal to point, it returns this node as the answer to the problem.

In the next part, the visit index should be set. This will further display the node's visibility status. From now on, the algorithm will behave like BFS. The difference is the addition of the heuristic function to the nodes.
```
        Node.heuristic = heuristic  # Setting all nodes heuristic functions
        heap = MinHeap()
        visited = set()
        root_node = Node(self.init_state)
        heap.add(root_node)
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
