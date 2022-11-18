class table:
    def __init__(self, Rows, Columns, Matrix, dataframe, vis):
        self.Rows = Rows
        self.Columns = Columns
        self.Matrix = Matrix
        self.vis = [[False for i in range(Rows)] for j in range(Columns)]
        
    #main costructors:
    def setdf(self):
        self.dataframe = pd.DataFrame(self.Matrix)
        #return df  
    def printdf(self):
        self.setdf()
        return self.dataframe
    def arrangedf(self):
        df = self.printdf()
        for i in range (0,self.Rows): 
            df[i] = df[i].str.replace('r', "")
            df[i] = df[i].str.replace('p', "")
            df[i] = df[i].str.replace('b', "")
            df[i] = df[i].replace('x', 999)  
                        
        return df
    
    def strtoint(self):
        df = self.arrangedf()
        for i in range (0,self.Rows):
            df[i] = df[i].astype(int)        
        #print(self.dataframe.dtypes) 
        return df
    
    #index:
    def robotindex(self):
        for i in range(self.Rows):
            for j in range(self.Columns):
                if "r" in self.Matrix[i][j]:
                    return ([i, j])
                
                
    def targetIndexes(self):
        """A function which returns index(es) of target(s)."""

        target_list = []
        for i in range(self.Rows):
            for j in range(self.Columns):
                if "p" in self.Matrix[i][j]:
                    target_list.append([i, j])
                    
        return target_list


    def butterIndexes(self):
        """A function which returns index(es) of butter(s)."""

        butter_list = []
        for i in range(self.Rows):
            for j in range(self.Columns):
                if "b" in self.Matrix[i][j]:
                    butter_list.append([i, j])
        return butter_list
        
    
    #DFS PART:
    #checking...
    
    def isCorner(self, row, col):
        if(row == 0 | row == self.Rows-1 | col == 0 | col == self.Columns-1):
            return True
        else:
            return False
        
    
    def isValid(self, row, col, matrix):
        ROW = self.Rows
        COL = self.Columns
        vis = self.vis

        # If cell is out of bounds
        if (row < 0 or col < 0 or row >= ROW or col >= COL):
            return False

        # If the cell is already visited
        if (vis[row][col]):
            return False

        # Otherwise, it can be visited
        return True

        # Otherwise, it can be visited
        return True
        
        
    def finish(self, row, col, tr, tc):
        if(row == tr & col == tc):
            return True
        else:
            return False
    
    #mai functions:  
    def dfs(self, row, col, tr, tc):
        print("start state: ",row,col)
        print("target state: ",tr,tc)
        
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]
        
        df = self.strtoint()
        st = []
        st.append([row, col])
        
        #print(self.vis)
        while (len(st) > 0):
            # Pop the top pair
            curr = st[len(st) - 1]
            st.remove(st[len(st) - 1])
            row = curr[0]
            col = curr[1]
            print(curr)
            # Check if the current popped
            # cell is a valid cell or not
            if (self.isValid(row, col, df) == False):
                continue

            # Mark the current
            # cell as visited
            self.vis[row][col] = True
            #print(self.vis)
            # Print the element at
            # the current top cell
            print(df[row][col], end = " ")

            # Push all the adjacent cells
            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                st.append([adjx, adjy])
                
                
    def printpath(self, row, col, tr, tc):
        saver = 0
        savec = 0
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
                #print(curr)
                #print(row, end = ",")
                #print(col, end = " ")
                continue


            self.vis[row][col] = True
            #print(row-saver, end = ",")
            #print(col-savec, end = " ")
            
            if(row-saver == 0):
                if(col-savec == 0):
                    print("stay", end =", ")
                if(col-savec == 1):
                    print("down", end =", ")
                if(col-savec == -1):
                    print("up", end =", ")
            if(col-savec == 0):
                if(row-saver == 0):
                    print("stay", end =", ")
                if(row-saver == 1):
                    print("right", end =", ")
                if(row-saver == -1):
                    print("left", end =", ")
                    
            saver = row
            savec = col
            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                st.append([adjx, adjy])
            if(self.finish(row, col, tr, tc)):
                break
                
            
