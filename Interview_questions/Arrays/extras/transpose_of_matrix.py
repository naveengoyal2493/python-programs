def transpose_matrix(list):
    new_list = []

    for i in range(len(list[0])):
        new_list.append([list[0][i]])

    for i in range(1, len(list)):
        for j in range(len(list[i])):
            new_list[j].append(list[i][j])

    return new_list

list = [[1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]]

print(transpose_matrix(list))
