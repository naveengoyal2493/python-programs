
from math import comb


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

# print(CountInversions().count_inversions([5,4,3,2]))

class CountReversePairs:
    def count_reverse_pairs(self, nums):
        pass

    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left_array = nums[:mid]
            right_array = nums[mid:]

            self.merge_sort(left_array)
            self.merge_sort(right_array)

            i, j = 0,0  
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

        
class FourSum:

    def four_sum(self, nums, target):
        nums.sort()
        quad, res = [], []

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

# print(FourSum().four_sum([1,0,-1,0,-2,2], 0))


def grid_unique_paths(m, n):
    row = [1] * n

    for i in range(m - 1):
        new_row = [1] * n
        for j in range(len(new_row) - 1, -1, -1):
            new_row[j - 1] = row[j-1] + new_row[j]
        row = new_row
    
    return row[0]

# print(grid_unique_paths(3, 6))

def maximum_subarray_sum(nums):
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(curr_sum, max_sum)

    return max_sum

# print(maximum_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))

def merge_overlapping_intervals(intervals):
    intervals.sort(key = lambda i: i[0])
    new_intervals = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = new_intervals[-1][1]
        if start <= last_end:
            new_intervals[-1][1] = max(end, last_end)
        else:
            new_intervals.append([start, end])

    return new_intervals

# print(merge_overlapping_intervals([[1,3],[5,10],[6,7], [2,5]]))  


def merge_two_sorted_arrays(arr1, arr2):
    left, right = 0, len(arr1) - 1

    while left < len(arr2) and right >= 0:
        if arr1[right] > arr2[left]:
            temp = arr1[right]
            arr1[right] = arr2[left]
            arr2[left] = temp

        left += 1
        right -= 1

    arr1.sort()
    arr2.sort()

    return arr1, arr2

arr1 = [1,3,5,7]
arr2 = [4,6,10]
# print(merge_two_sorted_arrays(arr1, arr2))

def search_2d_matrix(matrix, num):
    top, bottom = 0, len(matrix) - 1

    while top < bottom:
        row = (top + bottom) // 2
        if num < matrix[row][0]:
            bottom = row - 1
        elif num > matrix[row][-1]:
            top = row + 1
        else:
            break

    if top > bottom:
        return False

    row = (top + bottom) // 2
    left, right = 0, len(matrix[row]) - 1

    while left <= right:
        mid = (left + right) // 2
        if num < matrix[row][mid]:
            right = mid - 1
        elif num > matrix[row][mid]:
            left = mid + 1
        else:
            return True
    return False

matrix = [  [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]]

# print(search_2d_matrix(matrix, 34))

def find_first_duplicate_element(nums):
    dict = {}
    min = -1

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] not in dict:
            dict[nums[i]] = 1
        else:
            min = i
    
    return min

# print(find_first_duplicate_element([]))

def find_majority_element_n_by_2(nums):
    candidate = nums[0]
    life = 0

    for num in nums:
        if candidate == num:
            life += 1
        elif life == 0:
            candidate = num
            life += 1
        else:
            life -= 1

    return candidate

# print(find_majority_element_n_by_2([2,2,2,2,2,3,3,3,3]))

def find_majority_element_n_by_3(nums):
    ans = []
    candidate1 = nums[0]
    life1 = 0

    candidate2 = nums[1]
    life2 = 0

    for num in nums:
        if num == candidate1:
            life1 += 1
        elif num == candidate2:
            life2 += 1
        elif life1 == 0:
            candidate1 = num
            life1 += 1
        elif life2 == 0:
            candidate2 = num
            life2 += 1
        else:
            life1 -= 1
            life2 -= 1

    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    if count1 > len(nums) // 3:
        ans.append(candidate1)
    if count2 > len(nums) // 3:
        ans.append(candidate2)

    return ans

# print(find_majority_element_n_by_3([0,0,0]))

def find_second_largest_element(nums):
    if len(nums) < 2:
        return -1

    largest = second_largest = -2147483648
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == -2147483648:
        return -1
    else:
        return second_largest

# print(find_second_largest_element([12, 35, 1, 10, 34, 1]))


def find_duplicate_number(nums):
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

# print(find_duplicate_number([1,3,4,2,5,6,2]))


def longest_integer_sequence(nums):
    nums_set = set(nums)
    largest = 0

    for num in nums:
        if (num - 1) not in nums_set:
            length = 0
            while (num + length) in nums_set:
                length += 1
            largest = max(length, largest)
    return largest

# print(longest_integer_sequence([100, 4, 200, 1, 3, 2]))



# class Hello:
#     def myfunc():
#         print("Hello")


# class Bye:
#     def myfunc():
#         print("Bye")

# class Total(Hello, Bye):
#     myfunc()


def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums:
        if (num - 1) in nums:
            continue
        length = 0
        while (num + length) in nums_set:
            length += 1
        longest = max(length, longest)

    return longest

# print(longest_consecutive_sequence([100,4,200,1,3,2]))


def largest_subarray_with_0_sum(nums):
    hash_map = {0:0}
    total_sum = 0
    max_length = 0

    for i in range(len(nums)):
        total_sum += nums[i]
        if total_sum not in hash_map:
            hash_map[total_sum] = i + 1
        else:
            total_length = i - hash_map[total_sum] + 1
            max_length = max(total_length, max_length)
    
    return max_length

# print(largest_subarray_with_0_sum([2,8,-3,-5,2,-4,6,1,2,1,-3,4]))


def two_sum(nums, target):
    hash_map = {}

    for i in range(len(nums)):
        number = target - nums[i]
        if number not in hash_map:
            hash_map[nums[i]] = i
        else:
            return [hash_map[number], i]


# print(two_sum([2,7,11,15], 9))

def two_sum_II(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left+1, right+1]

def three_sum(nums):
    combs = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] + a < 0:
                left += 1
            elif nums[left] + nums[right] + a > 0:
                right -= 1
            else:
                combs.append([a, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return combs

# print(three_sum([-1,0,1,2,-1,-4]))

def three_sum(nums):
    combs = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and nums[i - 1] == a:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            if a + nums[left] + nums[right] < 0:
                left += 1
            elif a + nums[left] + nums[right] > 0:
                right -= 1
            else:
                combs.append([a, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return combs

# print(three_sum([-1,0,1,2,-1,-4]))

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

print(four_sum([1,0,-1,0,-2,2], 0))
