import numpy as np
import pandas as pd


class table:
    def __init__(self, Rows, Columns, Matrix, dataframe):
        self.Rows = Rows
        self.Columns = Columns
        self.Matrix = Matrix
        
    def setdf(self):
        self.dataframe = pd.DataFrame(self.Matrix)
        #return df
        
    def printdf(self):
        self.setdf()
        return self.dataframe
    
    
    
    def robotindex(self):
        for i in range(self.Rows):
            for j in range(self.Columns):
                if "r" in self.Matrix[i][j]:
                    return ([i, j])
                
                
    def targetIndexes(self):
        for i in range(self.Rows):
            for j in range(self.Columns):
                if "p" in self.Matrix[i][j]:
                    return ([i, j])
        
        
# An example code to take matrix input by user  
Rows = int(input("Give the number of rows:"))  
Columns = int(input("Give the number of columns:"))  
# Initializing the matrix  
matrix = []  
  
# taking RowsxColumns matrix from the user  
for i in range(Rows):  
    # taking input for the row from the user  
    single_row = list(map(str, input().split()))  
    # appending the 'single_row' to the 'example_matrix'  
    matrix.append(single_row)  
# printing the matrix given by user  
#print(matrix)  


t1 = table(Rows, Columns, matrix, "")
#t1.setdf()
t1.printdf()

# a function which returns index(es) of butter(s)
def butterIndexes(matrix, Rows, Columns):
    for i in range(Rows):
        for j in range(Columns):
            if "b" in matrix[i][j]:
                print(i, j)


# a function which returns index of the robot
def robotIndex(matrix, Rows, Columns):
    for i in range(Rows):
        for j in range(Columns):
            if "r" in matrix[i][j]:
                print(i, j)


# a function which returns index(es) of target(s)
def targetIndexes(matrix, Rows, Columns):
    for i in range(Rows):
        for j in range(Columns):
            if "p" in matrix[i][j]:
                print(i, j)
