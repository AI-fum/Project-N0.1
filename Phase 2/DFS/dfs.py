class table:
    def __init__(self, Rows, Columns, Matrix, dataframe, vis):
        self.Rows = Rows
        self.Columns = Columns
        self.Matrix = Matrix
        self.vis = [[0 for i in range(Rows)] for j in range(Columns)]
        
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
        
    def index_2d(self, myList, v):
        for i, x in enumerate(myList):
            if v in x:
                return (i, x.index(v)) 
    #DFS PART:
    #checking...
    
    def isCorner(self, row, col):
        if(row == 0 | row == self.Rows-1 | col == 0 | col == self.Columns-1):
            return True
        else:
            return False
        
    
    def isValid(self, row, col):
        ROW = self.Rows
        COL = self.Columns
        df = self.strtoint()
        # If cell is out of bounds
        #if (row < 0 or col < 0 or row >= ROW or col >= COL or matrix[row][col]>100):
            #return False
        if (row < 0 or col < 0 or row >= ROW or col >= COL):
            #print("invalid index!")
            return False
        if(df[row][col]>100):
            #print("Warning!!!")
            return False
        if(self.vis[row][col] > 0):
            return False
        # If the cell is already visited
        

        # Otherwise, it can be visited
        return True
        
    def isNeighbour(self, r1, r2, c1, c2):
        if(c1 == c2):
            if(r2 == r1+1 or r2 == r1-1):
                return True
        if(r1 == r2):
            if(c2 == c1+1 or c2 == c1-1):
                return True
        
        return False
    
    def getNeighbour(self, row, col):
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]
        st = []
        df = self.strtoint()
        for i in range(4):
            r = row + dRow[i]
            c = col + dCol[i]
            if(self.isValid(r, c) == True):
                st.append([r, c])
                
        return st
    
    def minNeighbour(self, row, col, df):
        l = []
        i = []
        row = int(row)
        col = int(col)
        d = self.strtoint()
        if(row == 0):
            #print("row is 0!")
            if(col == 0):
                #print("col is 0!")
                #print("corner...")
                if(d[row+1][col]<999):
                    l.append(df[row+1][col])
                    i.append([row+1, col])
                if(d[row][col+1]<999):
                    l.append(df[row][col+1])
                    i.append([row, col+1])
            if(col == self.Columns-1):
                #print("col is CLM!")
                #print("corner...")
                if(d[row][col-1]<999):
                    l.append(df[row][col-1]) 
                    i.append([row, col-1])
                if(d[row+1][col]<999):
                    l.append(df[row+1][col]) 
                    i.append([row+1, col])
            if(col >0 and col < self.Columns-1):
                #print("UP edge!")
                if(d[row][col-1]<999):
                    l.append(df[row][col-1])
                    i.append([row, col-1])
                if(d[row][col+1]<999):
                    l.append(df[row][col+1])
                    i.append([row, col+1])
                if(d[row+1][col]<999):
                    l.append(df[row+1][col])
                    i.append([row+1, col])
                
        if(row == self.Rows-1):
            #print("row is RWS!")
            if(col >0 and col < self.Columns-1):
                #print("Right edge!")
                if(d[row][col-1]<999):
                    l.append(df[row][col-1])
                    i.append([row, col-1])
                if(d[row][col+1]<999):
                    l.append(df[row][col+1])
                    i.append([row, col+1])
                if(d[row-1][col]<999):
                    l.append(df[row-1][col])
                    i.append([row-1, col])
                
        if(col == self.Columns-1): 
            #print("col is CLM!")
            if(row >0 and row < self.Rows-1):
                #print("Down edge!")
                if(d[row][col-1]<999):
                    l.append(df[row][col-1])
                    i.append([row, col-1])
                if(d[row-1][col]<999):
                    l.append(df[row-1][col])
                    i.append([row-1, col])
                if(d[row+1][col]<999):
                    l.append(df[row+1][col])
                    i.append([row+1, col])
                
        if(col == 0):
            #print("col is 0!")
            if(row == 0):
                #print("row is 0!")
                #print("corner...")
                if(d[row][col+1]<999):
                    l.append(df[row][col+1])
                    i.append([row, col+1])
                if(d[row+1][col]<999):
                    l.append(df[row+1][col])
                    i.append([row+1, col])
            if(row == self.Rows-1):
                #print("row is RWS!")
                #print("corner...")
                if(d[row][col+1]<999):
                    l.append(df[row][col+1])  
                    i.append([row, col+1])
                if(d[row-1][col]<999):
                    l.append(df[row-1][col])
                    i.append([row-1, col])
            if(row >0 and row < self.Rows-1):
                #print("Left edge!")
                if(d[row][col+1]<999):
                    l.append(df[row][col+1])
                    i.append([row, col+1])
                if(d[row-1][col]<999):
                    l.append(df[row-1][col])
                    i.append([row-1, col])
                if(d[row+1][col]<999):
                    l.append(df[row+1][col])
                    i.append([row+1, col])
                
                
        if(row != 0 and col !=0 and row != self.Rows-1 and col != self.Columns-1):
            if(d[row][col-1]<999):
                l.append(df[row][col-1])
                i.append([row, col-1])
            if(d[row][col+1]<999):
                l.append(df[row][col+1])
                i.append([row, col+1])
            if(d[row-1][col]<999):
                l.append(df[row-1][col])
                i.append([row-1, col])
            if(d[row+1][col]<999):
                l.append(df[row+1][col])
                i.append([row+1, col])
            
        #print("minimume neighbour of ", df[row][col], "is: ")
        ans = min(l)
        #print(l, ans)
        ans = l.index(ans)
        return i[ans]
    
    
    def finish(self, row, col, tr, tc):
        if(row == tr & col == tc):
            return True
        else:
            return False
    
    #mai functions:  
    #main functions:
    def dfs2(self, startr, startc, endr, endc):
        disc = [];
        prev = [];
        S = []
        df = self.strtoint()
        start = df[startr][startc]
        end = df[endr][endc]
        #push on stack
        S.append([startr, startc])
        print("start form ", startr, startc)
        print("value is: ", df[startr][startc])
        neighbour = self.getNeighbour(startr, startc)
        if(self.isValid(startr, startc)):
            print("neighbours: ", neighbour)
            
        for i in range (0, len(neighbour)):
            print("neighbour nubmer ", i, "is: ", neighbour[i])
        while(len(S) > 0):
            print("hello while")
            curr = S[len(S) - 1]
            disc.append(curr)
            
            for i in range (0, len(neighbour)):
                print("neighbour nubmer ", i, "is: ", neighbour[i])
                n = neighbour[i]

                if n not in disc:
                    if(all(n) == end):
                        print("TOOOOMAAAAAMMMMM")
                        break
                else:
                    S.append(n)
        
        
        
    def dfs(self, row, col, tr, tc):
        print("start state: ",row,col)
        print("target state: ",tr,tc)
        
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]
        
        df = self.strtoint()
        st = []
        st.append([row, col])
        path = []
        saver = row
        savec = col
        
        #print(self.vis)
        while (len(st) > 0):
            # Pop the top pair
            curr = st[len(st) - 1]
            st.remove(st[len(st) - 1])
            row = curr[0]
            col = curr[1]
            #print(curr)
            # Check if the current popped
            # cell is a valid cell or not
            if (self.isValid(row, col) == False):
                continue
                
                
            if(self.isNeighbour(saver, row, savec, col) == False):
                print("ohok")
                ind = self.minNeighbour(saver, savec, self.vis)
                row = ind[0]
                col = ind[1]
                
            print("from ",saver ,savec," to ", row, col, " : ", row-saver, col-savec)
            if(row-saver == 0):
                if(col-savec == 0):
                    path.append("stay")
                if(col-savec == -1):
                    path.append("UP")
                if(col-savec == 1):
                    path.append("DOWN")
                    
            if(row-saver == 1):
                path.append("RIGHT")
            if(row-saver == -1):
                path.append("LEFT")
            saver = row
            savec = col
            # Mark the current
            # cell as visited
            visave = self.vis[row][col]
            self.vis[row][col] = visave+1
            #print(self.vis)
            # Print the element at
            # the current top cell
            print(df[row][col], end = " ")

            # Push all the adjacent cells
            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                st.append([adjx, adjy])
                
            if(row == tr and col == tc):
                break
                
    def printpath(self, row, col, tr, tc):
        print("start state: ",row,col)
        print("target state: ",tr,tc)
        saver = 0
        savec = 0
        
        dRow = [0, 1, 0, -1]
        dCol = [-1, 0, 1, 0]
        path = []
        df = self.strtoint()
        st = []
        st.append([row, col])
        saver = row
        savec = col
        
        #print(self.vis)
        while (len(st) > 0):
            # Pop the top pair
            curr = st[len(st) - 1]
            st.remove(st[len(st) - 1])
            row = curr[0]
            col = curr[1]
            
            if (self.isValid(row, col, df) == False):
                print("ha")
                continue
            
            if(self.isNeighbour(saver, row, savec, col) == False):
                st.append(curr)
                m = self.minNeighbour(row, col, self.vis)
                row = m[0]
                col = m[1]
                if (self.isValid(row, col, df) == False):
                    print("jdscjbd'vpbd'psvc'pb")
            #save index:
            
            
            
            #print(curr)
            # Check if the current popped
            # cell is a valid cell or not
           
             
                
            print("from ",saver ,savec," to ", row, col, " : ", row-saver, col-savec)
            if(row-saver == 0):
                if(col-savec == 0):
                    path.append("stay")
                if(col-savec == -1):
                    path.append("UP")
                if(col-savec == 1):
                    path.append("DOWN")
                    
            if(row-saver == 1):
                path.append("RIGHT")
            if(row-saver == -1):
                path.append("LEFT")
            saver = row
            savec = col
            
                

            # Mark the current
            # cell as visited
            self.vis[row][col] = self.vis[row][col]+1
            #print(self.vis)
            # Print the element at
            # the current top cell
            print(df[row][col], end = " ")

            # Push all the adjacent cells
            for i in range(4):
                adjx = row + dRow[i]
                adjy = col + dCol[i]
                st.append([adjx, adjy])
                
        print(path) 
