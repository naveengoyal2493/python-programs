# input = [[1,2,3],[4,5,6],[7,8,9]]

from configparser import MAX_INTERPOLATION_DEPTH


def rotate_matrix_by_90(input):
    l, r = 0, len(input) - 1
    
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            topLeft = input[top][l + i]
            input[top][l + i] = input[bottom - i][l]
            input[bottom - i][l] = input[bottom][r - i]
            input[bottom][r - i] = input[top + i][r]
            input[top + i][r] = topLeft
        
        r -= 1
        l += 1
    return input
input = [   [1,2,3,4],
            [4,5,6,7],
            [7,8,9,1], 
            [1,2,3,4]]
# print(rotate_matrix_by_90(input))



