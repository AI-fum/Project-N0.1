from battlefield import Battlefield
from successor import State
from node import Node
from min_heap import MinHeap

battlefield: Battlefield
init_state: State


def ucs(self) -> Node:
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
