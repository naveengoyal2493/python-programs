class Solution:
    def searchMatrix(self, matrix, to_find: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top < bot:
            row = (top + bot) // 2
            if to_find < matrix[row][0]:
                bot = row - 1
            elif to_find > matrix[row][-1]:
                top = row + 1
            else:
                break

        if top > bot:
            return False

        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if to_find < matrix[row][m]:
                r = m - 1
            elif to_find > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False

matrix = [  [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]]
# matrix = [[1]]
print(Solution().searchMatrix(matrix, 5))