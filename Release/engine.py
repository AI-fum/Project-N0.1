from map import Map
from file_io import FileIO
from constants import Consts
from screen_manager import Display
from state import State
from node import Node
from heap_hashtable import MinHeap
import time


class GameManager:

    map: Map
    init_state: State
    display: Display

    def __init__(self):
        self.map, self.init_state = self.parse_map()
        # After parsing map it's time to start pygame
        self.display = Display(self.map)

    def start_search(self, search_type: str) -> (list[State], int, int):
        """ Chooses a search between all and returns its result list.
            :param search_type Search algorithm type
            :returns The result of search """

        result = self.__getattribute__(search_type + '_search')()

        # Putting path to goal in list
        if search_type in ['bd_bfs', 'reverse_bfs']:
            return result
        else:
            result_list = GameManager.extract_path_list(result)
            result_list.pop()
            result_list.reverse()
            return result_list, result.depth, result.path_cost

    def display_states(self, states_list: list[State]) -> None:
        """ Gets a list of states and displays it into display object.
            :param states_list List of states to show """

        if len(states_list) <= 0:
            print('There is no way')
            return

        self.display.update(self.init_state)                            # Starting display
        self.display.begin_display()

        for state in states_list:
            time.sleep(Consts.STEP_TIME)
            self.display.update(state)


    def bfs_search(self) -> Node:

        frontier = [Node(self.init_state)]
        visited = {}

        while len(frontier) > 0:  # Starting BFS loop
            node_1 = frontier.pop(0)
            visited[node_1.state] = node_1

            if State.is_goal(node_1.state, self.map.points):
                return node_1

            actions = State.successor(node_1.state, self.map)  # Add successors to frontier
            for child in node_1.expand(actions):
                if child.state not in visited:
                    frontier.append(child)
                    
    def dfs_search(self) -> Node:

        frontier = [Node(self.init_state)]
        visited = {}

        while len(frontier) > 0:  # Starting BFS loop
            node_1 = frontier.pop(0)
            visited[node_1.state] = node_1

            if State.is_goal(node_1.state, self.map.points):
                return node_1

            actions = State.successor(node_1.state, self.map)  # Add successors to frontier
            child = node_1.infiltrate(actions)
            if child.state not in visited:
                frontier.append(child)         
                    

    @staticmethod
    def parse_map() -> (Map, State):
        """ Uses map file to create map object in game.
            :returns The map object and the init state"""

        map_array = FileIO.read_line_by_line(Consts.MAP_FILE)
        sizes = map_array.pop(0)
        h, w = int(sizes[0]), int(sizes[1])
        map_object = Map(h, w)

        butters = []                                            # Variables to read from map
        points = []
        robot = (0, 0)
        for j, row in enumerate(map_array):
            for i, col in enumerate(row):

                if len(col) > 1:                                # If there is an object in map
                    if col[1] == 'b':
                        butters.append((j, i))
                    elif col[1] == 'p':
                        points.append((j, i))
                    elif col[1] == 'r':
                        robot = (j, i)
                    row[i] = col[0]

            map_object.append_row(row)                          # Append row to map

        map_object.set_points(points)
        return map_object, State(robot, butters)

    @staticmethod
    def extract_path_list(node: Node) -> list[State]:
        """ Gets a node and returns a list of states which contains all states from root to the node.
            :param node The node to get its path
            :returns The list of all states from root to the node"""

        result_list = []
        watchdog = 0
        while node is not None:
            watchdog += 1
            if watchdog > 1000:
                raise Exception('Watchdog limit exceeded')
            result_list.append(node.state)
            node = node.parent

        return result_list

    @staticmethod
    def state_in_list_of_nodes(state: State, nodes_list: list[Node]) -> bool:
        for node in nodes_list:
            if node.state == state:
                return True
        return False
