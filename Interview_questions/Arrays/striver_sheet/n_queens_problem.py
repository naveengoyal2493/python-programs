def n_queens_problem(n):
    posDiag = set()
    negDiag = set()
    cols = set()
    result = []

    board = [["."] * n for r in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
    
        for c in range(n):
            if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                continue

            posDiag.add(r + c)
            negDiag.add(r - c)
            cols.add(c)
            board[r][c] = "Q"

            backtrack(r + 1)

            posDiag.remove(r + c)
            negDiag.remove(r - c)
            cols.remove(c)
            board[r][c] = "."

    backtrack(0)
    return result

print(n_queens_problem(4))