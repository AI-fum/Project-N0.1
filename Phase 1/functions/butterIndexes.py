def butterIndexes(matrix, Rows, Columns):
    """A function which returns index(es) of butter(s)."""

    butter_list = []
    for i in range(Rows):
        for j in range(Columns):
            if "b" in matrix[i][j]:
                butter_list.append([i, j])
    return butter_list
