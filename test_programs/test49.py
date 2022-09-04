
from heapq import merge
from multiprocessing.reduction import duplicate
from socket import dup


class CountInversions:
    def count_inversions_in_array(self, nums):
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

# print(CountInversions().count_inversions_in_array([5,4,3,2]))


class CountReversePairs:
    
    def count_reverse_pairs(self, nums):
        self.reverse_pairs = []
        self.merge_sort(nums)
        return self.reverse_pairs

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
                    self.reverse_pairs.append([left_array[i], right_array[j]])
                    j += 1
                else:
                    i += 1

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

# print(CountReversePairs().count_reverse_pairs([2,4,3,5,1]))

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

# print(find_duplicate_number([1,2,3,1,4]))

def find_majority_element_n_by_2(nums):
    candidate = 0
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

# print(find_majority_element_n_by_2([2,5,3,1,4,4,4,4,4,]))

def find_majority_element_n_by_3(nums):
    ans = []
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
        if candidate1 == nums[i]:
            count1 += 1
        elif candidate2 == nums[i]:
            count2 += 1

    if count1 > len(nums) // 3:
        ans.append(candidate1)
    if count2 > len(nums) // 3:
        ans.append(candidate2)

    return ans
# print(find_majority_element_n_by_3([0,0,0]))

def find_repeating_and_missing(nums):
    for i in range(len(nums)):
        x = abs(nums[i]) - 1
        if nums[x] < 0:
            duplicate = abs(nums[i])
        else:
            nums[x] = -nums[x]

    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            break

    return duplicate, missing

# print(find_repeating_and_missing([1,2,4,5,6,7,6]))

def find_unique_paths(m, n):
    row = [1] * n
    for i in range(m - 1):
        new_row = [1] * n
        for j in range(n - 2, -1, -1):
            new_row[j] = new_row[j+1] + row[j]
        row = new_row
    return row[0]

# print(find_unique_paths(3,7))

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
    intervals.sort(key = lambda a: a[0])
    new_intervals = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = new_intervals[-1][1]
        if start <= last_end:
            new_intervals[-1][1] = max(end, last_end)
        else:
            new_intervals.append([start, end])

    return new_intervals

# print(merge_overlapping_intervals([[1,3],[5,10],[6,7], [2,5]]))

def merge_two_sorted_array(arr1, arr2):
    right = len(arr1) - 1
    left = 0

    while right >= 0 and left < len(arr2):
        if arr1[right] > arr2[left]:
            temp = arr2[left]
            arr2[left] = arr1[right]
            arr1[right] = temp

        right -= 1
        left += 1

    arr1.sort()
    arr2.sort()

    return arr1, arr2

arr1 = [1,3,5,7]
arr2 = [4,6,10]
# print(merge_two_sorted_array(arr1, arr2))


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
        while dec >= 0 and nums[dec] >= nums[dec + 1]:
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

# print(pascals_triangle(4))

class PowOfXN:
    def pow_of_x_n(self, x, n):
        result = self.helper(x, abs(n))
        return result if n >= 0 else 1 / result

    def helper(self, x, n):
        if x == 0: return 0
        if n == 0: return 1

        multiply = self.helper(x * x, n // 2)
        return multiply if n % 2 == 0 else multiply * x


# print(PowOfXN().pow_of_x_n(2,-10))

def rotate_matrix_by_90(matrix):
    left, right = 0, len(matrix) - 1
    i = 0
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
# print(rotate_matrix_by_90(input))

def search_in_2d_matrix(matrix):
    
