
from os import link


def longest_substring_without_repeating_characters(string):
    str_set = set()
    l = 0
    res = 0

    for r in range(len(string)):
        while string[r] in str_set:
            str_set.remove(string[l])
            l += 1
        str_set.add(string[r])
        res = max(res, r - l + 1)

    return res

# print(longest_substring_without_repeating_characters("abcabcbb"))

def largest_subarray_with_0_sum(nums):
    sum_dict = {0:0}
    longest = 0
    total_sum = 0

    for i in range(len(nums)):
        total_sum += nums[i]
        if total_sum in sum_dict:
            length = i - sum_dict[total_sum] + 1
            longest = max(longest, length)
        else:
            sum_dict[total_sum] = i + 1

    return longest

# print(largest_subarray_with_0_sum([2,8,-3,-5,2,-4,6,1,2,1,-3,4]))

def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest = 0
    for num in nums_set:
        if (num - 1) in nums_set:
            continue
        length = 0
        while (num + length) in nums_set:
            length += 1
        longest = max(longest, length)

    return longest

# print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

def four_sum(nums, target):
    nums.sort()
    res, quad = [], []
    
    def k_sum(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                k_sum(k - 1, i + 1, target - nums[i])
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
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    k_sum(4, 0, 0)
    return res

# print(four_sum([1,0,-1,0,-2,2], 0))

def three_sum(nums, target):
    nums.sort()
    res = []

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] + a < target:
                left += 1
            elif nums[left] + nums[right] + a > target: 
                right -= 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return res

# print(three_sum([-1,0,1,2,-1,-4], 0))

def two_sum_II(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return ([left + 1, right + 1])

# print(two_sum_II([1,3,4,5,7,10,11], 9))


def two_sum(nums, target):
    already = {}

    for index, value in enumerate(nums):
        to_find = target - value
        if to_find not in already:
            already[value] = index
        else:
            return (already[to_find], index)

# print(two_sum([7,3,4,8,9,1], 8))


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

            i,j = 0,0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] > 2 * right_array[j]:
                    self.count += len(left_array) - i
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

# print(ReversePairs().reverse_pairs([2,4,3,5,1]))

def grid_unique_paths(m, n):
    row = [1] * n

    for i in range(m - 1):
        new_row = [1] * n
        for j in range(len(new_row) - 2, -1, -1):
            new_row[j] = new_row[j + 1] + row[j]
        row = new_row

    return row[0]

# print(grid_unique_paths(3,6))

def majority_element_n_by_3(nums):
    ans = []
    candidate1 = 0
    life1 = 0

    candidate2 = 0
    life2 = 0

    for num in nums:
        if candidate1 == num:
            life1 += 1
        elif candidate2 == num:
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

    count1 = 0
    count2 = 0

    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1

    if count1 >= len(nums) / 3:
        ans.append(candidate1)
    if count2 >= len(nums) / 3:
        ans.append(candidate2)

    return ans

# print(majority_element_n_by_3([0,0,0]))

def find_majority_element_n_by_2(nums):
    candidate = 0
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


def helper(x, n):
    res = pow_of_x_n(x, abs(n))
    return res if n > 0 else 1/res

def pow_of_x_n(x, n):
    if x == 0: return 0
    if n == 0: return 1
    res = pow_of_x_n(x*x, n // 2)
    return res if n % 2 == 0 else res * x

# print(helper(2,-10))

def search_in_a_2d_matrix(matrix, num):
    top, bottom = 0, len(matrix) - 1

    while top < bottom:
        mid_row = (top + bottom) // 2
        if num < matrix[mid_row][0]:
            bottom = mid_row - 1
        elif num > matrix[mid_row][-1]:
            top = mid_row + 1
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

# print(search_in_a_2d_matrix(matrix, 11))

class CountInversions:

    def count_inversions_in_an_array(self, nums):
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

# print(CountInversions().count_inversions_in_an_array([5,4,3,2]))

def find_duplicate_and_missing_number(nums):
    for i in range(len(nums)):
        x = abs(nums[i]) - 1
        if nums[x] < 0:
            duplicate = abs(x) + 1
        else:
            nums[x] = -nums[x]

    for j in range(len(nums)):
        if nums[j] > 0:
            missing = j + 1
            break

    return (duplicate, missing)

# print(find_duplicate_and_missing_number([1,1,5,4,3]))
def find_duplicate(nums):
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

# print(find_duplicate([1,3,4,2,5,6,2]))

def merge_two_sorted_arrays(arr1, arr2):
    right, left = len(arr1) - 1, 0

    while right >= 0 and left < len(arr2):
        if arr1[right] > arr2[left]:
            temp = arr1[right]
            arr1[right] = arr2[left]
            arr2[left] = temp

        left += 1
        right -= 1

    arr1.sort()
    arr2.sort()
    return (arr1, arr2)

arr1 = [1,3,5,7]
arr2 = [4,6,10]
# print(merge_two_sorted_arrays(arr1, arr2))

def merge_overlapping_sub_intervals(intervals):
    intervals.sort(key = lambda i: i[0])
    new_invervals = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = new_invervals[-1][1]
        if start <= last_end:
            new_invervals[-1][1] = max(last_end, end)
        else:
            new_invervals.append([start, end])

    return new_invervals
# input = [[1,3],[5,10],[6,7], [2,5]]
# print(merge_overlapping_sub_intervals(input))


def rotate_matrix(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom  = left, right
            temp = matrix[top][left + i]
            matrix[top][left + 1] = matrix[bottom - i][left]
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
# print(rotate_matrix(matrix))

def stock_buy_and_sell(prices):
    left, right = 0, 1
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            curr_profit = prices[right] - prices[left]
            max_profit = max(curr_profit, max_profit)
        else:
            left = right
        right += 1
    
    return max_profit

# print(stock_buy_and_sell([7,1,5,3,6,4]))

def sort_array_of_0s_1s_and_2s(nums):
    left, right = 0, len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            temp = nums[left]
            nums[left] = nums[i]
            nums[i] = temp
            left += 1
        elif nums[i] == 2:
            temp = nums[right]
            nums[right] = nums[i]
            nums[i] = temp
            right -= 1
            i -= 1
        i += 1
    return nums

# print(sort_array_of_0s_1s_and_2s([2,0,2,1,1,0,0,1,1,2,2,1,2,1,0,0,0,2,1,2]))

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
        while nums[next_num] <= nums[dec] and next_num < len(nums):
            next_num += 1
        self.swap(nums, next_num, dec)

        return nums

# print(NextPermutation().next_permutation([1,5,4,3,2]))

def pascals_triangle(n):
    res = [[1]]

    for i in range(n - 1):
        temp_array = [0] + res[-1] + [0]
        row = []
        for j in range(len(temp_array) - 1):
            row.append(temp_array[j] + temp_array[j + 1])
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

def sort_array_of_0s_1s_and_2s_again(nums):
    left, right = 0, len(nums) - 1
    i = 0

    while i <= right:
        if nums[i] == 0:
            temp = nums[left]
            nums[left] = nums[i]
            nums[i] = temp
            left += 1
        elif nums[i] == 2:
            temp = nums[right]
            nums[right] = nums[i]
            nums[i] = temp
            i -= 1
            right -= 1

        i += 1

    return nums           

# print(sort_array_of_0s_1s_and_2s_again([2,0,2,1,1,0,1,1,1,0,0,0,0,2,2,2,1,1,1,0,0,2,2,1,1,2,2,1,1,1]))

def stocks_buy_and_sell_again(prices):
    left, right = 0, 1
    max_profit = 0
    curr_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            curr_profit = prices[right] - prices[left]
            max_profit = max(curr_profit, max_profit)
        else:
            left =right
        right += 1

    return max_profit

# print(stocks_buy_and_sell_again([7,1,5,3,6,4]))

def stocks_buy_and_sell_again_again(prices):
    left, right = 0, 1
    max_profit = 0
    curr_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            curr_profit = prices[right] - prices[left]
            max_profit = max(curr_profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit

# print(stocks_buy_and_sell_again_again([7,1,5,3,6,4]))

def rotate_matrix_again(matrix):
    left, right = 0, len(matrix[0]) - 1

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
# print(rotate_matrix_again(input))

def find_duplicate_in_array_again(nums):
    slow = 0
    fast = 0
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

# print(find_duplicate_in_array_again([1,3,4,2,5,6,2]))

def find_first_duplicate_element(nums):
    already = {}
    min = -1

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] in already:
            min = i
        else:
            already[nums[i]] = i

    return min

# print(find_first_duplicate_element([1,2,3,4,5,6,6]))

def largest_subarray_with_0_sum(nums):
    already = {0:0}
    longest = 0
    total_sum = nums[0]

    for index, value in enumerate(nums):
        if total_sum in already:
            length = index - already[total_sum] + 1
            longest = max(length, longest)
        else:
            already[total_sum] = index + 1
        total_sum += value

    return longest

# print(largest_subarray_with_0_sum([2,8,-3,-5,2,-4,6,1,2,1,-3,4]))

def find_second_largest_element(nums):
    first = second = -2147483648

    for num in nums:
        if first < num:
            second = first
            first = num
        elif second < num and second != first:
            second = num

    return second

# print(find_second_largest_element([12, 35, 1, 10, 34, 1]))


class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self, head = None):
        self.head = head

    def insert_element_at_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_element_at_end(self, data):
        if not self.head:
            self.insert_element_at_beginning(data)

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_list(self, list):
        for num in list:
            self.insert_element_at_end(num)

    def print(self):
        if not self.head:
            raise "Linked list is empty"
        itr = self.head
        linklist = ""
        while itr:
            linklist += str(itr.data) + "-->"
            itr = itr.next
        print(linklist)


ll = LinkedList()
ll.insert_list([1,2,3,4,5])

def reverse_linked_list(linked_list):
    prev = None
    curr = linked_list.head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

# new_node = reverse_linked_list(ll)
# ll2 = LinkedList(new_node)
# ll2.print()

def find_middle_of_linked_list(linked_list):
    itr = linked_list.head
    slow = itr
    fast = itr

    while fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            break
    
    return slow


# new_node = find_middle_of_linked_list(ll)
# ll3 = LinkedList(new_node)
# ll3.print()


def merge_two_sorted_linked_list(l1, l2):
    list1 = l1.head
    list2 = l2.head
    new_list = nl = Node(0, None)

    while list1 and list2:
        if list1.data < list2.data:
            new_list.next = Node(list1.data, None)
            list1 = list1.next
        else:
            new_list.next = Node(list2.data, None)
            list2 = list2.next
        new_list = new_list.next

    if list1:
        new_list.next = list1

    if list2:
        new_list.next = list2

    return nl.next

# l1 = LinkedList()
# l1.insert_list([1,3,5,7,9])
# l2 = LinkedList()
# l2.insert_list([2,4,6,8,10])

# new_list = merge_two_sorted_linked_list(l1, l2)
# l3 = LinkedList(new_list)
# l3.print()











    


        