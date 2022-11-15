# a function which returns index(es) of target(s)
def targetIndexes(matrix, Rows, Columns):
    for i in range(Rows):
        for j in range(Columns):
            if "p" in matrix[i][j]:
                print(i, j)
