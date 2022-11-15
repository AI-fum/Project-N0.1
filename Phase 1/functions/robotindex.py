# a function which returns index of the robot
def robotIndex(matrix, Rows, Columns):
    for i in range(Rows):
        for j in range(Columns):
            if "r" in matrix[i][j]:
                print(i, j)
