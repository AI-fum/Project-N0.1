def targetIndexes(matrix, Rows, Columns):
    """A function which returns index(es) of target(s)."""

    target_list = []
    for i in range(Rows):
        for j in range(Columns):
            if "p" in matrix[i][j]:
                target_list.append([i, j])
    return target_list
