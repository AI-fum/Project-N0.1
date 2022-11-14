dRow = [0, 1, 0, -1]
dCol = [-1, 0, 1, 0]
vis = [[False for i in range(3)] for j in range(3)]
def isValid(row, col, matrix):
    global ROW
    global COL
    global vis
    if (row < 0 or col < 0 or row >= ROW or col >= COL or matrix[row][col]>100):
        return False
    if (vis[row][col]):
        return False
    return True


def finish(row, col, tr, tc):
    if(row == tr and col == tc):
        return True
    else:
        return False


def dfs(row, col, grid, tr, tc):
    global dRow
    global dCol
    global vis

    # Initialize a stack of pairs and
    # push the starting cell into it
    st = []
    st.append([row, col])

    # Iterate until the
    # stack is not empty
    while (len(st) > 0):
        # Pop the top pair
        curr = st[len(st) - 1]
        st.remove(st[len(st) - 1])
        row = curr[0]
        col = curr[1]
        # Check if the current popped
        # cell is a valid cell or not
        if (isValid(row, col, grid) == False):
            continue
            

            
        # Mark the current
        # cell as visited
        vis[row][col] = True
        # Print the element at
        # the current top cell
        print(grid[row][col], end = " ")
        # Push all the adjacent cells
        for i in range(4):
            adjx = row + dRow[i]
            adjy = col + dCol[i]
            st.append([adjx, adjy])
            
        if(finish(row, col, tr, tc)):
            break
            
if __name__ == '__main__':
    grid = [[1, 999, 3],
            [4, 5, 6],
            [7, 8, 9]]

    # Function call
    dfs(0, 0, grid, 2, 1)
    
    
    # BBBBBBBBBBBBBBBBBBLLLLLLLLLLLLLLLOOOOOOOOOOOOOOOOOOOOOOOBBBBBBBBBBBBBLLLLLLLLLLLLLLLLLLLLOOOOOOOOOOOOOOOO
    
    class table:
    def __init__(self, Rows, Columns, Matrix, dataframe, vis):
        self.Rows = Rows
        self.Columns = Columns
        self.Matrix = Matrix
        self.vis = [[False for i in range(Rows)] for j in range(Columns)]
        
    def setdf(self):
        self.dataframe = pd.DataFrame(self.Matrix)
        #return df
        
    def printdf(self):
        self.setdf()
        return self.dataframe
    
    def arrangedf(self):
        df = self.printdf()
        for i in range (0,self.Rows):
            df[i] = df[i].replace('x', 9999)
            
        return df
    
    def isValid(self, row, col, matrix):
    if (row < 0 or col< 0 or row >= self.Rows or col >= self.Columns  or matrix[row][col]>100):
        return False
    if (self.vis[row][col]):
        return False
    return True

    def finish(row, col, tr, tc):
        if(row == tr and col == tc):
            return True
        else:
            return False
