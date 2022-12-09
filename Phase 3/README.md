## A*
Acorrdig to wikipedia A* (pronounced "A-star") is a graph traversal and path search algorithm, which is used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches; however, A* is still the best solution in many cases.

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
In next step, we must call the heuristic function for each node.
