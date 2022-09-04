from audioop import mul
from cProfile import run
from pydoc import Helper
from turtle import left, right


def stocks_buy_and_sell(prices):
    left, right = 0, 1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right

        right += 1

    return max_profit

# print(stocks_buy_and_sell([1,10,9,2,1,8]))

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    return nums

def sort_array_of_012(nums):
    left, right = 0, len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums = swap(nums, left, i)
            left += 1
        elif nums[i] == 2:
            nums = swap(nums, i, right)
            right -= 1
            i -= 1
        i += 1

    return nums

# print(sort_array_of_012([1,1,1,1,2,2,2,2,0,0,0,0,2,1,0,0,1,1,1]))

def set_matrix_zero(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0

    if row_zero:
        for c in range(cols):
            matrix[0][c] = 0

    return matrix
# matrix = [[0,1,1],[1,1,1],[1,1,0]]
# print(set_matrix_zero(matrix))

def search_in_2d_matrix(matrix, target):
    TOP, BOTTOM = 0, len(matrix) - 1

    while TOP < BOTTOM:
        row_mid = (TOP + BOTTOM) // 2
        if target < matrix[row_mid][0]:
            BOTTOM = row_mid - 1
        elif target > matrix[row_mid][-1]:
            TOP = row_mid + 1
        else:
            break
    
    if TOP > BOTTOM:
        return False

    row_mid = (TOP + BOTTOM) // 2
    left, right = 0, len(matrix[0]) - 1

    while left <= right:
        mid = (left + right) // 2
        if target < matrix[row_mid][mid]:
            right = mid - 1
        elif target > matrix[row_mid][mid]:
            left = mid + 1
        else:
            return True
    return False

matrix = [  [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]]

# print(search_in_2d_matrix(matrix, 11))

def rotate_matrix_by_90(matrix):
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

input = [   [1,2,3,4],
            [4,5,6,7],
            [7,8,9,1], 
            [1,2,3,4]]
# print(rotate_matrix_by_90(input))

class PowXN:

    def helper(self, x, n):
        res = self.pow_x_n(x, abs(n))
        return res if n > 0 else 1/res
    def pow_x_n(self, x, n):
        if x == 0: return 0
        if n == 0: return 1

        even_pow = self.pow_x_n(x * x, n // 2)
        return even_pow * x if n % 2 != 0 else even_pow

# print(PowXN().helper(2,10))

def pascals_triangle(n):
    res = [[1]]
    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res

# print(pascals_triangle(5))

class NextPermutation:
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1

    def next_permutation(self, nums):
        if len(nums) == 1:
            return nums 
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
        dec = len(nums) - 2
        while nums[dec] >= nums[dec + 1] and dec >= 0:
            dec -= 1
        self.reverse(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return nums
        next_num = dec + 1
        while nums[dec] >= nums[next_num] and next_num < len(nums):
            next_num += 1
        self.swap(nums, next_num, dec)

        return nums

# print(NextPermutation().next_permutation([1,5,4,3,2]))

def merge_sorted_array(arr1, arr2):
    up = len(arr1) - 1
    down = 0

    while up >= 0 and down < len(arr1) - 1:
        if arr1[up] > arr2[down]:
            temp = arr2[down]
            arr2[down] = arr1[up]
            arr1[up] = temp
        up -= 1
        down += 1

    arr1.sort()
    arr2.sort()

    return arr1, arr2

# arr1 = [1,3,5,7]
# arr2 = [4,6,10]
# print(merge_sorted_array(arr1, arr2))

def merge_sort_algo(nums, count=0):
    if len(nums) > 1:
        mid = len(nums) // 2
        left_array = nums[:mid]
        right_array = nums[mid:]

        merge_sort_algo(left_array, count)
        merge_sort_algo(right_array, count)

        i,j,k = 0,0,0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                nums[k] = left_array[i]
                i += 1
            else:
                nums[k] = right_array[j]
                j += 1
                count += len(left_array) - i
            k += 1

        while i < len(left_array):
            nums[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            nums[k] = right_array[j]
            j += 1
            k += 1

    return count

# print(merge_sort_algo([4,2,5,7,8,1,2,4,5,6]))

def merge_overlapping_intervals(intervals):
    intervals.sort(key = lambda i: i[0])
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

def maximum_subarray_sum(nums):
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(curr_sum, max_sum)

    return max_sum

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(maximum_subarray_sum(arr))

def grid_unique_paths(m, n):
    row = [1] * n
    for i in range(m - 1):
        new_row = [1] * n
        for j in range(len(new_row) - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row
    return new_row[0]

# print(grid_unique_paths(3,6))

def find_repeating_and_missing_numbers(nums):
    k = 0
    for i in range(len(nums)):
        x = abs(nums[i]) - 1
        if nums[x] < 0:
            repeating = x + 1
        else:
            nums[x] = -nums[x]
    
    for j in range(len(nums)):
        if nums[j] > 0:
            missing = j + 1
            break

    return repeating, missing

# print(find_repeating_and_missing_numbers([1,1,5,4,3]))

def find_majority_element_n_by_2(nums):
    candidate = nums[0]
    life = 0

    for i in range(len(nums)):
        if candidate == nums[i]:
            life += 1
        elif life == 0:
            candidate = nums[i]
            life += 1
        else:
            life -= 1

    return candidate

# print(find_majority_element_n_by_2([2,3,2,3,2,3,2,3,1,2,1,2,1,2,2,3,3,3,3,3]))

def find_majority_element_n_by_3(nums):
    candidate1 = 0
    candidate2 = 0
    life1 = 0
    life2 = 0

    for i in range(len(nums)):
        if candidate1 == nums[i]:
            life1 += 1
        elif candidate2 == nums[i]:
            life2 += 1
        elif life1 == 0:
            candidate1 = nums[i]
            life1 += 1
        elif life2 == 0:
            candidate2 = nums[i]
            life2 += 1
        else:
            life1 -= 1
            life2 -= 1

    count1 = 0
    count2 = 0
    for i in range(len(nums)):
        if nums[i] == candidate1:
            count1 += 1
        elif nums[i] == candidate2:
            count2 += 1

    arr = []
    if count1 > len(nums) // 3:
        arr.append(candidate1)
    if count1 > len(nums) // 3:
        arr.append(candidate2)

    return arr

# print(find_majority_element_n_by_3([0,0,0]))

