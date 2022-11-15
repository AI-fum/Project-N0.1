def get_matrix(Rows, Columns):
    # Initializing the matrix  
    matrix = []  
    # taking RowsxColumns matrix from the user  
    for i in range(Rows):  
        # taking input for the row from the user  
        single_row = list(map(str, input().split()))  
        # appending the 'single_row' to the 'example_matrix'  
        matrix.append(single_row)
    return(matrix)
    
