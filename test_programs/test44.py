a = [1,3,5,7]
b = [2,4,6]

def merge_two_sorted_arrays(arr1, arr2):
    i, j = len(arr1) - 1, 0
    while i >=0 and j < len(arr2):
        if arr2[j] < arr1[i]:
            temp = arr2[j]
            arr2[j] = arr1[i]
            arr1[i] = temp
        
        i -= 1
        j += 1
    
    arr1.sort()
    arr2.sort()

    return arr1, arr2


# print(merge_two_sorted_arrays(a, b))

class NextPermutation:
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

# print(NextPermutation().next_permutation([1,2,4,3,5]))
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

# input = [[1,3],[5,10],[6,7],[2,5]]
# print(merge_overlapping_intervals(input))

def pascals_triangle(n):
    res = [[1]]
    for _ in range(n - 1):
        temp = [0] + res[-1] + [0]
        rows = []
        for j in range(len(temp) - 1):
            rows.append(temp[j] + temp[j + 1])
        res.append(rows)
    return res

# print(pascals_triangle(5))

def maximum_subarray_sum(nums):
    max_sum = 0
    curr_sum = nums[0]
    for num in nums:
        if curr_sum <= 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(curr_sum, max_sum)
    return max_sum

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(maximum_subarray_sum(arr))
    
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
# input = [   [1,2,3,4],
#             [4,5,6,7],
#             [7,8,9,1], 
#             [1,2,3,4]]
# print(rotate_matrix_by_90_degrees(input))

def find_repeating_and_missing_numbers(nums):
    for i in range(len(nums)):
        x = abs(nums[i]) - 1
        if nums[x] < 0:
            repeating = abs(nums[i])
        else:
            nums[x] = -nums[x]

    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            break

    return (repeating, missing)
    

# input = [4,2,4,1,3]
# print(find_repeating_and_missing_numbers(input))

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

# matrix = [  [0, 1, 1],
#             [1, 1, 1],
#             [1, 1, 0]]
# print(set_matrix_zero(matrix))


def find_duplicate_number(nums):
    slow, fast = 0,0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

# nums = [3,1,2,4,3]
# print(find_duplicate_number(nums))

def swap(nums, ind1, ind2):
    temp = nums[ind1]
    nums[ind1] = nums[ind2]
    nums[ind2] = temp
    return nums

def sort_array(nums):
    left, right = 0, len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums = swap(nums, left, i)
            left += 1
        if nums[i] == 2:
            nums = swap(nums, i, right)
            right -= 1
            i -= 1

        i += 1
    return nums

# print(sort_array([1,1,1,1,1,2,0,2,1,1,0,0,1,1,1,1,1,1,2,2,2,2,2,0,0,0,0,0]))

def stocks_buy_and_sell(nums):
    left, right = 0, 1
    max_profit = 0
    while right < len(nums):
        if nums[left] > nums[right]:
            left = right
        else:
            profit = nums[right] - nums[left]
            max_profit = max(profit, max_profit)
        right += 1

    return max_profit

# print(stocks_buy_and_sell([2,6,3,1,1]))
        