class table:
    def __init__(self, Rows, Columns, Matrix):
        self.Rows = Rows
        self.Columns = Columns
        self.Matrix = Matrix
        
    def setdf(self):
        df = pd.DataFrame(self.Matrix)
        #return df
        
        
# An example code to take matrix input by user  
  
Rows = int(input("Give the number of rows:"))  
Columns = int(input("Give the number of columns:"))  
  
# Initializing the matrix  
example_matrix = []  
  
# taking RowsxColumns matrix from the user  
for i in range(Rows):  
    # taking input for the row from the user  
    single_row = list(map(str, input().split()))  
    # appending the 'single_row' to the 'example_matrix'  
    example_matrix.append(single_row)  
# printing the matrix given by user  
#print(example_matrix)  


t1 = table(Rows, Columns, example_matrix)
t1.setdf()
