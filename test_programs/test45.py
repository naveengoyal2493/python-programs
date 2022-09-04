class Solution:
    def count_inversions_in_array(self, nums):
        self.count = 0
        self.helper(nums)
        return self.count

    def helper(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left_array = nums[:mid]
            right_array = nums[mid:]

            self.helper(left_array)
            self.helper(right_array)

            i,j,k = 0,0,0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    nums[k] = left_array[i]
                    i += 1
                else:
                    nums[k] = right_array[j]
                    j += 1
                    self.count += len(left_array) - i
                k += 1
            
            while i < len(left_array):
                nums[k] = left_array[i]
                i += 1
                k += 1

            while j < len(right_array):
                nums[k] = right_array[j]
                j += 1
                k += 1

        return nums

# print(Solution().count_inversions_in_array([5,3,6,1,8,4]))

def find_duplicate_number(nums):
    fast, slow = 0, 0
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]

        if fast == slow:
            break

    slow2 = 0
    while True:
        slow2 = nums[slow2]
        slow = nums[slow]
        if slow2 == slow:
            return slow

# print(find_duplicate_number([1,2,3,4,1]))

def find_repeating_and_missing_numbers(nums):
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

# print(find_repeating_and_missing_numbers([5,3,3,2,1]))

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

def merge_overlapping_intervals(intervals):
    intervals.sort(key = lambda a: a[0])
    new_intervals = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = new_intervals[-1][1]
        if last_end >= start:
            new_intervals[-1][1] = max(last_end, end)
        else:
            new_intervals.append([start, end])

    return new_intervals
# input = [[1,3],[5,10],[6,7], [2,5]]
# print(merge_overlapping_intervals(input))

def merge_sort_algorithm(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left_array = nums[:mid]
        right_array = nums[mid:]

        merge_sort_algorithm(left_array)
        merge_sort_algorithm(right_array)

        i,j,k = 0,0,0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                nums[k] = left_array[i]
                i += 1
            else:
                nums[k] = right_array[j]
                j += 1
            k += 1
        
        while i < len(left_array):
            nums[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            nums[k] = right_array[j]
            j += 1
            k += 1

    return nums

# print(merge_sort_algorithm([1,4,7,2,7,9,3,11,4,7,8,2,1,5,7,9,2]))

def merge_two_sorted_arrays(arr1, arr2):
    l = len(arr1) - 1
    r = 0

    while l >= 0 and r < len(arr2):
        if arr1[l] > arr2[r]:
            temp = arr1[l]
            arr1[l] = arr2[r]
            arr2[r] = temp
        l -= 1
        r += 1
    
    arr1.sort()
    arr2.sort()

    return arr1, arr2

# arr1 = [1,3,5,7]
# arr2 = [4,6,10]
# print(merge_two_sorted_arrays(arr1, arr2))

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
            return self.swap(nums, 0 ,1)
        dec = len(nums) - 2
        while nums[dec] >= nums[dec + 1] and dec >= 0:
            dec -= 1
        self.reverse(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return nums
        next_num = dec + 1
        while nums[next_num] <= nums[dec] and next_num < len(nums):
            next_num += 1
        self.swap(nums, next_num, dec)

        return nums

# print(NextPermutation().next_permutation([1,5,4,3,2]))

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

class PowerOfN:
    def helper(self, x, n):
        res = self.power_of_x_n(x, abs(n))
        return res if n >= 0 else 1 / res

    def power_of_x_n(self, x, n):
        if x == 0: return 0
        if n == 0: return 1
        res = self.power_of_x_n(x*x, n // 2)
        return res * x if n % 2 != 0 else res

# print(PowerOfN().helper(2,-10))

def rotate_matrix_by_90(matrix):
    l, r = 0, len(matrix) - 1
    i = 0

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            temp = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = temp

        r -= 1
        l += 1

    return matrix
input = [   [1,2,3,4],
            [4,5,6,7],
            [7,8,9,1], 
            [1,2,3,4]]
# print(rotate_matrix_by_90(input))

def search_in_2d_matrix(matrix, target):
    top, bottom = 0, len(matrix) - 1
    while top < bottom:
        row = (top + bottom) // 2
        if target < matrix[row][0]:
            bottom = row - 1
        elif target > matrix[row][-1]:
            top = row + 1
        else:
            break

    if top > bottom:
        return False

    row = (top + bottom) // 2
    l, r = 0, len(matrix[0]) - 1
    while l <= r:
        mid = (l + r) // 2
        if target < matrix[row][mid]:
            r = mid - 1
        elif target > matrix[row][mid]:
            l = mid + 1
        else:
            return True

    return False

# matrix = [  [1,3,5,7],
#             [10,11,16,20],
#             [23,30,34,60]]
# matrix = [[1]]
# print(search_in_2d_matrix(matrix, 2))

def set_matrix_zero(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    row_zero = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0 
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if row_zero:
        for c in range(COLS):
            matrix[0][c] = 0

    return matrix
# matrix = [[0,1,1],[1,1,1],[1,1,0]]
# print(set_matrix_zero(matrix))

def swap(nums, left, right):
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp

    return nums

def sort_array_of_1s_2s(nums):
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

# print(sort_array_of_1s_2s([1,1,1,1,1,2,2,2,2,0,0,0,0,1,1,0,0,2,2,2,1,1,0,0,2,2]))

def stocks_buy_and_sell(prices):
    left, right = 0, 1
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right

        right += 1

    return max_profit

# print(stocks_buy_and_sell([5,4,7,10]))
