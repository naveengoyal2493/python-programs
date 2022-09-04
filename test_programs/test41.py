def rotate_matrix_by_90_degrees(matrix):
    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            temp = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = temp

        left += 1
        right -= 1

    return matrix

# matrix = [  [1,2,3,4],
#             [5,6,7,8],
#             [9,1,2,3],
#             [4,5,6,7]]
# print(rotate_matrix_by_90_degrees(matrix))


def merge_overlapping_intervals(intervals):
    intervals.sort(key= lambda i: i[0])
    new_intervals = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = new_intervals[-1][1]
        if start <= last_end:
            new_intervals[-1][1] = max(last_end, end)
        else:
            new_intervals.append([start, end])

    return new_intervals

# input = [[1,3],[5,10],[6,7], [2,5]]
# print(merge_overlapping_intervals(input))

def merge_two_sorted_arrays_without_space(arr1, arr2):
    i, j = len(arr1) - 1, 0
    while i >= 0 and j < len(arr2):
        if arr1[i] > arr2[j]:
            temp = arr1[i]
            arr1[i] = arr2[j]
            arr2[j] = temp
        i -= 1
        j += 1
    
    arr1.sort()
    arr2.sort()
    return (arr1, arr2)

arr1 = [5,6,2,8]
arr2 = [1,7,3]

print(merge_two_sorted_arrays_without_space(arr1, arr2))