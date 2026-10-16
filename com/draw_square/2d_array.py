def addm(A, B):
    result = []
    i = 0
    while i < len(A): # loop every row
        row = []
        j = 0
    while j < len(A[i]): # loop every column
        row.append( A[i][j] + B[i][j] )
        j = j + 1
        result.append( row )
        i = i + 1
    return result

