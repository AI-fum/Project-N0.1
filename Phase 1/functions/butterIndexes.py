# a function which returns index(es) of butter(s)
def butterIndexes(matrix, Rows, Columns):
    for i in range(Rows):
        for j in range(Columns):
            if "b" in matrix[i][j]:
                print(i, j)
