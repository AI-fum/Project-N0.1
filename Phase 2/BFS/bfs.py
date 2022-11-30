from battlefield import Battlefield
from successor import State
from node import Node

init_state = State  #initial state...

def bfs() -> Node:
  queue = [Node(init_state)]
  vis = {}  #visited nodes

  while len(queue) > 0:  # Starting BFS loop
    current_node = queue.pop(0)
    vis[node_1.state] = current_node

    if State.is_goal(current_node.state, self.map.points):
      return current_node

    actions = State.successor(current_node.state, self.map)  # Add successors to queue
      for child in current_node.expand(actions):
        if child.state not in vis:
          queue.append(child)
