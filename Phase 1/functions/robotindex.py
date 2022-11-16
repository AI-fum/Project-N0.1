def robotIndex(matrix, Rows, Columns):
    """A function which returns index of the robot."""

    for i in range(Rows):
        for j in range(Columns):
            if "r" in matrix[i][j]:
                return[i, j]
