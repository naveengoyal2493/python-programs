

def longest_substring_without_repeat(string):
    string_set = set()
    longest = 0
    left = 0

    for letter in string:
        while letter in string_set:
            string_set.remove(string[left])
            left += 1
        string_set.add(letter)
        longest = max(len(string_set), longest)

    return longest

# print(longest_substring_without_repeat("abcabcbb"))


def largest_subarray_with_0_sum(nums):
    already = {0:0}
    longest = 0
    total_sum = 0

    for i in range(len(nums)):
        total_sum += nums[i]
        if total_sum not in already:
            already[total_sum] = i + 1
        else:
            length = i - already[total_sum] + 1
            longest = max(longest, length)

    return longest

# print(largest_subarray_with_0_sum([2,8,-3,-5,2,-4,6,1,2,1,-3,4]))

def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest = 0
    for num in nums_set:
        if (num - 1) not in nums_set:
            length = 0
            while (num + length) in nums_set:
                length += 1
            longest = max(longest, length)
    return longest

# print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

def four_sum(nums, target):
    nums.sort()
    res, quad = [] , []

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
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] + nums[i] < 0:
                left += 1
            elif nums[left] + nums[right] + nums[i] > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return res

# print(three_sum([-1,0,1,2,-1,-4]))

def two_sum_II(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left+1, right+1]
    return

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

            while i < len(left_array) and  j < len(right_array):
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

def grid_unique_paths(m, n):
    row = [1] * n

    for i in range(m - 1):
        new_row = [1] * n
        for j in range(n - 1, -1, -1):
            new_row[j - 1] = new_row[j] + row[j - 1]
        row = new_row

    return row[0]

# print(grid_unique_paths(3,6))

def mejority_element_n_by_3(nums):
    ans = []
    candidate1 = 0
    life1 = 0

    candidate2 = 0
    life2 = 0

    for num in nums:
        if candidate1 == num:
            life1 += 1
        elif life1 == 0:
            candidate1 = num
            life1 += 1
        elif candidate2 == num:
            life2 += 1
        elif life2 == 0:
            candidate2 = num
            life2 += 1
        else:
            life1 -= 1
            life2 -= 1
    
    count1, count2 = 0,0
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1

    if count1 > len(nums) / 3:
        ans.append(candidate1)
    if count2 > len(nums) / 3:
        ans.append(candidate2)

    return ans

# print(mejority_element_n_by_3([0,0,0]))

def majority_element_n_by_2(nums):
    life = 0
    candidate = 0

    for num in nums:
        if candidate == num:
            life += 1
        elif life == 0:
            candidate = num
            life += 1
        else:
            life -= 1
    return candidate

# print(majority_element_n_by_2([2,2,2,2,2,3,3,3,3]))

class PowXN:

    def pow_x_n(self, x, n):
        res = self.pow(x, abs(n))
        return res if n > 0 else 1/res

    def pow(self, x, n):
        if x == 0: return 0
        if n == 0: return 1

        res = self.pow(x*x, n // 2)
        return res if n % 2 == 0 else res * x

# print(PowXN().pow_x_n(2,-10))

def search_in_2d_matrix(matrix, to_find):
    top, bottom = 0, len(matrix)
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

    left, right = 0, len(matrix[0])
    while left < right:
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
print(search_in_2d_matrix(matrix, 35))