number1 = [[2,5],[6,8],[0,9]]
number2 = [[6,9],[2,3],[4,5]]

def add_matrix(matrix1, matrix2):
   
    result = [[0, 0], [0, 0], [0, 0]]
   
   
    for i in range(len(matrix1)):        
        for j in range(len(matrix1[0])):  
           
            result[i][j] = matrix1[i][j] + matrix2[i][j]
           
    return result


print(add_matrix(number1, number2))

def subtract_matrix(matrix1, matrix2):
   
    result = [[0, 0], [0, 0], [0, 0]]
   
   
    for i in range(len(matrix1)):        
        for j in range(len(matrix1[0])):  
           
            result[i][j] = matrix1[i][j] - matrix2[i][j]
           
    return result


print(subtract_matrix(number1, number2))

def multiplication_matrix(matrix1, matrix2):

    result = [[0, 0], [0, 0], [0, 0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] * matrix2[i][j]
    return result

print(multiplication_matrix(number1, number2))
