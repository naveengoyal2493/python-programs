# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire 
# column and row to 0 and then return the matrix.

"""Examples 1:
Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0"""

def set_matrix_zero(matrix):
    index = []
    for i in range(len(matrix)):
        if 0 in matrix[i]:
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    index.append(j)
            matrix[i] = [0] * len(matrix[i])


    for k in range(len(matrix)):
        for i in index: 
            matrix[k][i] = 0

    return matrix
    
# matrix=[[1,1,1],[1,0,1],[1,1,1]]
# print(set_matrix_zero(matrix))
# matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(set_matrix_zero(matrix))



def print_matrix(matrix):
    for matric in matrix:
        print(matric)
        
    print("")

# O(1) memory solution
def set_zeros(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False
    # which rows and columns need to be zeros
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True

    print_matrix(matrix)
    
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    print_matrix(matrix)

    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0
    
    print_matrix(matrix)
    
    if row_zero:
        for c in range(cols):
            matrix[0][c] = 0

    print_matrix(matrix)

matrix = [[0,1,1],[1,1,1],[1,1,0]]
print_matrix(matrix)
set_zeros(matrix)
