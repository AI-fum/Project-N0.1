from battlefield import Battlefield
from successor import State
from node import Node

battlefield: Battlefield
init_state: State  # initial state...
goal_state: State  # goal state ...

def manhattan_distance(current, goal):
    # Initialize the distance to 0
    distance = 0

    # Loop through the dimensions of the state
    for i in range(len(current)):
        # Calculate the absolute difference in the current dimension
        diff = abs(current[i] - goal[i])

        # Add the difference to the total distance
        distance += diff

    # Return the total distance
    return distance

def a_star(self) -> Node:
    queue = [(0, Node(init_state))]  # Initialize the queue with the root node
    vis = {}  # Dictionary to keep track of visited nodes

    # Loop until the queue is empty
    while len(queue) > 0:
        # Pop the next node from the queue
        current_node = queue.pop(0)[1]
        vis[current_node.state] = current_node

        # Check if the node is the goal
        if State.is_goal(current_node.state, self.battlefield.points):
            # Return the goal node
            return current_node

        # Generate the successor nodes for the current node
        actions = State.successor(current_node.state, battlefield)
        for child in current_node.expand(actions):
            # Calculate the cost of the child node
            cost = current_node.cost + State.cost(child.state, battlefield)
            # Calculate the heuristic value using the Manhattan distance
            heuristic = manhattan_distance(child.state, goal_state)

            # Add the child to the queue if it has not been visited
            if child.state not in vis:
                queue.append((cost + heuristic, child))

        # Sort the queue by cost
        queue.sort(key=lambda item: item[0])

    # If the search failed, return None
    return None
