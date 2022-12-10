
def iterative_deepening_search(matrix, start, goal, max_depth):
    for depth_limit in range(max_depth):
        visited = set()
        stack = [(start, 0)]
        while stack:
            (current, depth) = stack.pop()
            if current in goal:
                return True
            if depth < depth_limit:
                for neighbor in get_neighbors(matrix, current):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append((neighbor, depth+1))
    return False


def get_neighbors(matrix, current):
    # Return the neighbors of the current cell in the matrix.
    (i, j) = current
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))  # Top neighbor
    if i < len(matrix)-1:
        neighbors.append((i+1, j))  # Bottom neighbor
    if j > 0:
        neighbors.append((i, j-1))  # Left neighbor
    if j < len(matrix[0])-1:
        neighbors.append((i, j+1))  # Right neighbor
    return neighbors

if __name__ == "__main__" :
    start = robot_state # initial state on robot ... 
    goals =  battlefield_state # list of state of battlefield
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    found = iterative_deepening_search(matrix, start, goals, max_depth=10)
    if found:
        print("Goal found!")
    else:
        print("Goal not found.")

