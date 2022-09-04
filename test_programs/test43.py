from heapq import merge
from operator import le


def maximum_subarray_sum(nums):
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum

# print(maximum_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))

def merge_overlapping_intervals(intervals):
    intervals.sort(key = lambda i: i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])

    return output

# input = [[1,3],[5,10],[6,7], [2,5]]
# print(merge_overlapping_intervals(input))

def merge_two_sorted_arrays_without_space(arr1, arr2):
    i, j = len(arr1) - 1, 0
    while i >= 0 and j < len(arr2):
        if arr2[j] < arr1[i]:
            temp = arr2[j]
            arr2[j] = arr1[i]
            arr1[i] = temp
        i -= 1
        j += 1

    arr1.sort()
    arr2.sort()
    return arr1, arr2

# arr1 = [5,6,7]    
# arr2 = [1,2,3,4]
# print(merge_two_sorted_arrays_without_space(arr1, arr2))


class Solution:
    def swap(self, nums, ind1, ind2):
        temp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = temp

    def reverse(self, nums, beg, end):
        while beg < end:
            self.swap(nums, beg, end)
            beg += 1
            end -= 1
        
    def next_permutation(self, nums):
        if len(nums) == 1:
            return
        if len(nums) == 2:
            self.swap(nums, 0, 1)
    
        dec = len(nums) - 2
        while dec >= 0 and nums[dec] >= nums[dec + 1]:
            dec -= 1
        self.reverse(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return nums
        next_num = dec + 1
        while nums[dec] >= nums[next_num] and next_num < len(nums):
            next_num += 1
        self.swap(nums, dec, next_num)
        return nums


# print(Solution().next_permutation([1,5,4,3,2]))

def pascals_triangle(n):
    res = [[1]]
    for _ in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for i in range(len(temp) - 1):
            row.append(temp[i] + temp[i + 1])
        res.append(row)
    return res

# print(pascals_triangle(4))

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
            if matrix[0][c] == 0 or matrix[r][0] == 0:
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

def swap(nums, ind1, ind2):
    temp = nums[ind1]
    nums[ind1] = nums[ind2]
    nums[ind2] = temp
    return nums

def sort_array_of_0s_1s_and_2s(nums):
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

# print(sort_array_of_0s_1s_and_2s([1,2,2,1,2,1,0,0,2,1,2,1,0]))

def stock_buy_and_sell(prices):
    left, right = 0, 1
    max_price = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            curr_price = prices[right] - prices[left]
            max_price = max(max_price, curr_price)
        else:
            left = right
        right += 1
    return max_price

# print(stock_buy_and_sell([5,2,7,1,3]))