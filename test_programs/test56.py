def longest_substring_without_repeat(string):
    new_string = set()
    left = 0
    longest = 0

    for letter in string:
        while letter in new_string:
            new_string.remove(string[left])
            left += 1
        new_string.add(letter)
        longest = max(len(new_string), longest)

    return longest

# print(longest_substring_without_repeat("abcabcbb"))

def largest_subarray_with_0_sum(nums):
    already = {0:0}
    longest = 0
    total_sum = 0

    for i in range(len(nums)):
        total_sum += nums[i]
        if total_sum in already:
            length = i - already[total_sum] + 1
            longest = max(length, longest)
        else:
            already[total_sum] = i + 1

    return longest

# print(largest_subarray_with_0_sum([2,8,-3,-5,2,-4,6,1,2,1,-3,4]))

def longest_integer_sequence(nums):
    nums = set(nums)
    longest = 0

    for num in nums:
        if (num - 1) in nums:
            continue
        length = 0
        while (num + length) in nums:
            length += 1
        longest = max(length, longest)
    return longest

# print(longest_integer_sequence([100, 4, 200, 1, 3, 2]))

def four_sum(nums, target):
    nums.sort()
    res, quad = [], []

    def k_sum(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                k_sum(k-1, i+1, target - nums[i])
                quad.pop()
            return

        left, right = start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                res.append(quad + [nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    k_sum(4, 0, target)
    return res

# print(four_sum([1,0,-1,0,-2,2], 0))

def three_sum(nums):
    ans = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right =  i + 1, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] + nums[i] < 0:
                left += 1
            elif nums[left] + nums[right] + nums[i] > 0:
                right -= 1
            else:
                ans.append([nums[left], nums[right], nums[i]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return ans

# print(three_sum([-1,0,1,2,-1,-4]))

def two_sum_II(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left + 1, right + 1]

# print(two_sum_II([1,3,4,5,7,10,11], 9))

class ReversePairs:
    def reverse_pairs(self, nums):
        self.count = 0
        self.merge_sort(nums)
        return self.count

    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left_array = nums[:mid]
            right_array = nums[mid:]

            self.merge_sort(left_array)
            self.merge_sort(right_array)

            i, j = 0, 0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] > 2 * right_array[j]:
                    self.count += len(left_array) - i
                    i += 1
                else:
                    j += 1

            i, j, k = 0, 0, 0
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

# print(ReversePairs().reverse_pairs([2,4,3,5,1]))


def search_in_2d_matrix(matrix, to_find):
    top, bottom = 0, len(matrix) - 1

    while top < bottom:
        mid_row = (top + bottom) // 2
        if to_find < matrix[mid_row][0]:
            bottom = mid_row - 1
        elif to_find > matrix[mid_row][-1]:
            top = mid_row + 1
        else:
            break

    if top > bottom:
        return False

    mid_row = (top + bottom) // 2
    left, right = 0, len(matrix[mid_row]) - 1

    while left <= right:
        mid = (left + right) // 2
        if to_find < matrix[mid_row][mid]:
            right = mid - 1
        elif to_find > matrix[mid_row][mid]:
            left = mid + 1
        else:
            return True

    return False

matrix = [  [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]]
# matrix = [[1]]
# print(search_in_2d_matrix(matrix, 1))

class CountInversions:
    def count_inversions(self, nums):
        self.count = 0
        self.merge_sort(nums)
        return self.count

    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left_array = nums[:mid]
            right_array = nums[mid:]

            self.merge_sort(left_array)
            self.merge_sort(right_array)

            i, j, k = 0, 0, 0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    nums[k] = left_array[i]
                    i += 1
                else:
                    nums[k] = right_array[j]
                    self.count += len(left_array) - i
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

# print(CountInversions().count_inversions([5,4,3,2]))

def find_repeat_and_missing_number(nums):
    for i in range(len(nums)):
        x = abs(nums[i]) - 1
        if nums[x] < 0:
            repeating = x + 1
        else:
            nums[x] = -nums[x]

    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            break

    return (repeating, missing)

# print(find_repeat_and_missing_number([1,1,5,4,3]))

def find_duplicate_in_an_array(nums):
    slow, fast = 0, 0
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

# print(find_duplicate_in_an_array([1,3,4,2,5,6,2]))

def merge_two_sorted_array(arr1, arr2):
    right, left = len(arr1) - 1, 0

    while right >= 0 and left < len(arr2):
        if arr2[left] < arr1[right]:
            temp = arr2[left]
            arr2[left] = arr1[right]
            arr1[right] = temp
        left += 1
        right -= 1

    arr1.sort()
    arr2.sort()

    return arr1, arr2

arr1 = [1,3,5,7]
arr2 = [4,6,10]
# print(merge_two_sorted_array(arr1, arr2))

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

def rotate_matrix(matrix):
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
# print(rotate_matrix(input))

def stocks_buy_and_sell(prices):
    max_profit = 0
    left, right = 0, 1

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit

# print(stocks_buy_and_sell([7,1,5,3,6,4]))
def swap(nums, ind1, ind2):
    temp = nums[ind1]
    nums[ind1] = nums[ind2]
    nums[ind2] = temp

    return nums
def sort_array_of_0s_1s_2s(nums):
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

# print(sort_array_of_0s_1s_2s([2,0,2,1,1,0,1,1,2,2,0,0,1,2,0,1,2,0,1,2,1,0,0,1,2]))

def kadanes_algorithm(nums):
    max_sum = 0
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(curr_sum, max_sum)
    return max_sum

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(kadanes_algorithm(arr))

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
            return self.reverse(nums, 0, 1)

        dec = len(nums) - 2

        while dec >= 0 and nums[dec] >= nums[dec + 1]:
            dec -= 1
        
        self.reverse(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return nums

        next_num = dec + 1
        while next_num < len(nums) and nums[dec] >= nums[next_num]:
            next_num += 1
        self.swap(nums, dec, next_num)
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

def find_first_duplicate_element(nums):
    already = {}
    min = -1

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] in already:
            min = i
        else:
            already[nums[i]] = 1

    return min

# print(find_first_duplicate_element([1,2,3,4,5,6,6,1]))

def find_second_largest_element(nums):
    if len(nums) < 2:
        return -1
    first = second = -2147483648

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    
    if second == -2147483648:
        return -1
    else:
        return second

# print(find_second_largest_element([12, 35, 1, 10, 34, 1]))

def find_all_permutations(nums):
    res = []
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = find_all_permutations(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)

    return res

# print(find_all_permutations([1,2,3]))


def permutation(nums):
    res = []
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutation(nums)
        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)

    return res

print(permutation([1,2,3]))


