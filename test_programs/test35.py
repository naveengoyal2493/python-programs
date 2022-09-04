from logging import root
import re


def pascals_triangle(n):
    res = [[1]]
    for _ in range(n):
        temp_array = [0] + res[-1] + [0]
        row = []        
        for index in range(len(res[-1]) + 1):
            row.append(temp_array[index] + temp_array[index + 1])
        res.append(row)
    return res

print(pascals_triangle(5))