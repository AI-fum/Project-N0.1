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
    
    def strtoint(self):
        df = self.arrangedf()
        for i in range (0,self.Rows):
            df[i] = df[i].astype(int)
            
        #print(self.dataframe.dtypes)
            
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
        
    def dfs(self, row, col, tr, tc):
        self.setdf()
        self.dataframe = self.arrangedf()
        #print(self.dataframe)
        self.dataframe = self.strtoint()
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]
        st = []
        st.append([row, col])
        while (len(st) > 0):
            curr = st[len(st) - 1]
            st.remove(st[len(st) - 1])
            row = curr[0]
            col = curr[1]
            if (self.isValid(row, col, self.dataframe) == False):
                continue


            self.vis[row][col] = True
            print(self.dataframe[row][col], end = " ")
            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                st.append([adjx, adjy])
            #if(self.finish(row, col, tr, tc)):
                #break
