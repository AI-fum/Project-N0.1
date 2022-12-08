## IDS

Iterative deepening search is a type of search algorithm that is used in artificial intelligence and computer science. It is a combination of depth-first search and breadth-first search, and it is useful for searching large spaces where the depth of the solution is not known in advance.

To implement iterative deepening search in Python, you would first need to define a function that performs depth-first search on a given search space. This function should take a starting node, a goal node, and the search space as input, and it should return a list of actions that lead from the starting node to the goal node.

Once you have defined this function, you can implement iterative deepening search by calling the depth-first search function multiple times, each time with a different depth limit. For example:

#### Sample implement

##### Code
def ids(start, goal, space):
    depth = 0
    while True:
        result = dfs(start, goal, space, depth)
        if result != None:
            return result
        depth += 1

This implementation of iterative deepening search will call the depth-first search function with increasing depth limits until a solution is found.
