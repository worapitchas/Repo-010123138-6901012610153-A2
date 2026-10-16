class matrix:
    
    def __init__(self, data):
        self.data = data

    def show(self):
        for row in self.data:
            print(row)
        print()

    def add(self, other):

        result = [[0, 0, 0], [0, 0, 0]]
        
        for i in range(len(self.data)):        
            for j in range(len(self.data[0])):  
                result[i][j] = self.data[i][j] + other.data[i][j]
           
        return matrix(result) 

    def subtract(self, other):
        result = [[0, 0, 0], [0, 0, 0]]
   
        for i in range(len(self.data)):        
            for j in range(len(self.data[0])):  
                result[i][j] = self.data[i][j] - other.data[i][j]
           
        return matrix(result)
    
    def multiplication(self, other):
        result = [[0, 0, 0], [0, 0, 0]]
        
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                result[i][j] = self.data[i][j] * other.data[i][j]
                
        return matrix(result)


number1 = [[2, 4, 5], [5, 6, 7]]
number2 = [[8, 7, 6], [1, 6, 3]]

matrix1 = matrix(number1)
matrix2 = matrix(number2)


matrix1.show()
matrix2.show()

result_add = matrix1.add(matrix2)
result_add.show()

result_sub = matrix1.subtract(matrix2)
result_sub.show()

result_mul = matrix1.multiplication(matrix2)
result_mul.show()
