from battlefield import Battlefield
from successor import State
from node import Node

battlefield: Battlefield
init_state: State  # initial state...


def bfs(self) -> Node:
    queue = [Node(init_state)]
    vis = {}  # visited nodes
    
    while len(queue) > 0:  # Starting BFS loop
        current_node = queue.pop(0)
        vis[current_node.state] = current_node

        if State.is_goal(current_node.state, self.map.points):
            return current_node

        actions = State.successor(
            current_node.state, battlefield
        )  # Add successors to queue
        for child in current_node.expand(actions):
            if child.state not in vis:
                queue.append(child)
