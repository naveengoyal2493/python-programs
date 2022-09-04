def find_unique_paths(m, n):
    row = [1] * n

    for _ in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row
    return row[0]

print(find_unique_paths(3,6))