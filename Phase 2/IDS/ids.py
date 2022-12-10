from battlefield import Battlefield
from successor import State
from node import Node

battlefield: Battlefield
init_state: State  # initial state...
max_depth = 1000

def ids(self) -> Node:
    depth = 0  # Initialize the depth to 0

    # Loop until the maximum depth is reached
    while depth <= max_depth:
        # Perform a depth-first search at the current depth
        result = self.dfs(depth)

        # Check if a solution was found
        if result is not None:
            # Return the solution node
            return result

        # Increment the depth
        depth += 1

    # If the search failed, return None
    return None

def dfs(self, depth) -> Node:
    stack = [Node(init_state)]  # Initialize the stack with the root node
    vis = {}  # Dictionary to keep track of visited nodes

    # Loop until the stack is empty
    while len(stack) > 0:
        # Pop the next node from the stack
        current_node = stack.pop()
        vis[current_node.state] = current_node
        # Check if the node is the goal
        if State.is_goal(current_node.state, self.battlefield.points):
            # Return the goal node
            return current_node
        # Check if the current depth has been reached
        if current_node.depth == depth:
            continue
        # Generate the successor nodes for the current node
        actions = State.successor(current_node.state, battlefield)
        for child in current_node.expand(actions):
            # Add the child to the stack if it has not been visited
            if child.state not in vis:
                stack.append(child)
    # If the search failed, return None
    return None
