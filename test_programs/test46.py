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
                if left_array[i] <= right_array[j]:
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
        
# nums = [5,4,3,2,1]
# print(CountInversions().count_inversions_in_array(nums))

def find_duplicate_number(nums):
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow2 = 0
    while True:
        slow2 = nums[slow2]
        slow = nums[slow]
        if slow == slow2:
            return slow

# print(find_duplicate_number([4,1,2,3,1]))

def find_majority_element(nums):
    res = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == res:
            count += 1
        else:
            if count == 0:
                res = nums[i]
                count += 1
            else:
                count -= 1
    
    return res

# print(find_majority_element([2,2,2,2,3,3,3]))

def find_repeating_and_missing_numbers(nums):
    i = 0
    while i < len(nums):
        x = abs(nums[i]) - 1
        if nums[x] < 0:
            repeating = abs(nums[x])
        else:
            nums[x] = -nums[x]
        i += 1

    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            break

    return repeating, missing

# nums = [6,1,2,4,5,5]
# print(find_repeating_and_missing_numbers(nums))

def maximum_subarray_sum(nums):
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(maximum_subarray_sum(arr))

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

# input = [[1,3],[5,10],[6,7], [2,5]]
# print(merge_overlapping_intervals(input))

def merge_two_sorted_arrays(arr1, arr2):
    up , down = len(arr1) - 1, 0

    while up >= 0 and down < len(arr2):
        if arr1[up] > arr2[down]:
            temp = arr1[up]
            arr1[up] = arr2[down]
            arr2[down] = temp
        up -= 1
        down += 1
        
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

def pascals_triangle(n):
    res = [[1]]
    for _ in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res

# print(pascals_triangle(5))

class PowOfN:
    def helper(self, x, n):
        res = self.pow_of_n(x, abs(n))
        return res if n > 0 else 1 / res

    def pow_of_n(self, x, n):
        if x == 0: return 0
        if n == 0: return 1

        res = self.pow_of_n(x*x, n // 2)
        return res if n % 2 == 0 else res * x

# print(PowOfN().helper(2, -10))

