from operator import le
import re


class NextPermutation:

    def swap(self, nums, ind1, ind2):
        temp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = temp
        return nums

    def reverse(self, nums, beg, end):
        while beg < end:
            nums = self.swap(nums, beg, end)
            beg += 1
            end -= 1
        return nums

    def next_permutation(self, nums):
        if len(nums) == 1:
            return
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
        dec = len(nums) - 2
        while nums[dec] >= nums[dec + 1] and dec >=0:
            dec -= 1
        nums = self.reverse(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return nums
        next_num = dec + 1
        while nums[next_num] <= nums[dec] and next_num < len(nums):
            next_num += 1
        nums = self.swap(nums, dec, next_num)
        return nums

# print(NextPermutation().next_permutation([1,2,3,4]))


def maximum_subarray(nums):
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum

# print(maximum_subarray([-1,2,-3,4,1]))

def pascals_triangle(n):
    res = [[1]]
    for _ in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res

# print(pascals_triangle(3))

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

def sort_array(nums):    
    left, right = 0, len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            swap(nums,left, i)
            left += 1
        elif nums[i] == 2:
            swap(nums,i, right)
            right -= 1
            i -= 1
        i += 1
    return nums

print(sort_array([2,2,1,1,0,0]))

# [1,4,2,6,3]

def stock_buy_and_sell(prices):
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1

    return max_profit

# print(stock_buy_and_sell([1,4,2,6,3]))