    def a_star_search(self) -> Node:
        def manhattan_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
            d1 = point1[0] - point2[0]
            d2 = point1[1] - point2[1]
            if d1 < 0:
                d1 = d1*(-1)
            if d2 < 0:
                d2 = d2*(-1)
         
            manhattan_distance = d1 + d2
            return manhattan_distance

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
        # Setting all nodes heuristic functions
        Node.heuristic = heuristic
        # Beginning of a star search
        heap = MinHeap()  
        visited = set()
        root_node = Node(self.init_state)
        heap.add(root_node)
        while not heap.is_empty():
            node = heap.pop()
            # Checking goal state
            if State.is_goal(node.state, self.battlefield.points):
                return node
            if node.state not in visited:
                visited.add(node.state)
            else:
                continue
            # A* search
            actions = State.successor(node.state, self.battlefield)
            for child in node.expand(actions):
                heap.add(child)
