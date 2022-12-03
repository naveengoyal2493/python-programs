from os import remove


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


# def permutation(nums):
#     res = []
#     if len(nums) == 1:
#         return [nums[:]]

#     for i in range(len(nums)):
#         n = nums.pop(0)
#         perms = permutation(nums)
#         for perm in perms:
#             perm.append(n)
#         res.extend(perms)
#         nums.append(n)

#     return res

# print(permutation([1,2,3]))



input = [[1,5,2,7,2,9,8,1,9], [1,5,3,4,4],[1,5,2,6]]
# input = [[5,5], [2,2]]
def cards_game(input):
    highest = []

    for list1 in input:
        already = {}
        numbers = []
        for i in list1:
            if i in already:
                already[i] += 1
            else:
                already[i] = 1

        for key in already.keys():
            if already[key] == 1:
                numbers.append(key)

        if not numbers:
            numbers.append(0)

        highest.append(max(numbers))

    return -1 if max(highest) == 0 else max(highest)

# print(cards_game(input))


def remove_duplicates(nums):
    left, right = 1, 1
    while right < len(nums):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
        right += 1
    return left + 1

# nums = [1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
# print(remove_duplicates(nums))


def count_max_consecutive_1s(nums):
    max_count = 0
    count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0

    return max_count

# nums = [1,1,1,0,0,1,1,1,1,1,0]
# print(count_max_consecutive_1s(nums))

def trapping_rainwater(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    max_left = height[left]
    max_right = height[right]
    res = 0

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, height[left])
            res += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            res += max_right -height[right]

    return res

# heights = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trapping_rainwater(heights))
    
def three_sum(nums):
    res = []
    nums.sort()

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
                res.append([nums[left], nums[right], nums[i]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return res

# print(three_sum([-1,0,1,2,-1,-4]))

class RandomListNode:

    def __init__(self, val, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random

def clone_a_linked_list(head):
    old_to_copy = {None : None}

    curr = head

    while curr:
        old_to_copy[curr] = RandomListNode(curr.val)
        curr = curr.next

    curr = head

    while curr:
        copy = old_to_copy[curr]
        copy.next = old_to_copy[curr.next]
        copy.random = old_to_copy[curr.random]
        curr = curr.next

    return old_to_copy[head]



class ListNode:

    def __init__(self, val, next):
        self.val = val
        self.next = next
  
class LinkedList:

    @staticmethod
    def insert_at_beginning(val, head = None):
        return ListNode(val, head)        

    @staticmethod
    def insert_values(values, head = None):
        for i in range(len(values) - 1, -1, -1):
            head = LinkedList.insert_at_beginning(values[i], head)
        return head

    @staticmethod
    def merge_two_linked_lists(firsthead, lasthead):
        itr = firsthead
        while itr.next:
            itr = itr.next
        itr.next = lasthead
        return firsthead
    
    @staticmethod
    def print_ll(head):
        if not head:
            return "Linked list is empty"
        itr = head
        ll = ""
        while itr:
            ll += str(itr.val) + "-->"
            itr = itr.next

        print(ll)


class TwoPointerListNode:

    def __init__(self, val, next=None, bottom=None):
        self.val = val
        self.next = next
        self.bottom = bottom

class NextAndRandomListNode:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def rotate_a_linked_list(head, k):
    tail = head

    length = 1
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if not k:
        return head

    curr = head
    for i in range(length - k - 1):
        curr = curr.next

    new_head = curr.next
    curr.next = None
    tail.next = head

    return new_head

# k = 2
# head = LinkedList.insert_values([1,2,3,4,5,6,7,8])
# rotate = rotate_a_linked_list(head, k)
# LinkedList.print_ll(rotate)


def flattening_a_linked_list(head):
    if not head:
        return None

    if not head.next:
        return head

    return helper(head, flattening_a_linked_list(head.next))

def helper(head1, head2):
    list3 = head3 = TwoPointerListNode(0)

    while head1 and head2:
        if head1.val < head2.val:
            list3.bottom = TwoPointerListNode(head1.val)
            head1 = head1.bottom
        else:
            list3.bottom = TwoPointerListNode(head2.val)
            head2 = head2.bottom
        list3 = list3.bottom

    if head1:
        list3.bottom = head1
    
    if head2:
        list3.bottom = head2

    return head3.bottom

l1 = TwoPointerListNode(5)
l1.next = TwoPointerListNode(6)
l1.next.next = TwoPointerListNode(8)
l1.next.next.bottom = TwoPointerListNode(11)
l1.next.next.bottom.bottom = TwoPointerListNode(12)
l1.next.bottom = TwoPointerListNode(10)
l1.bottom = TwoPointerListNode(7)
l1.bottom.bottom = TwoPointerListNode(9)

# head = flattening_a_linked_list(l1)
# while head:
#     print(head.val)
#     head = head.bottom


def find_the_starting_point_of_loop(head):
    if not head:
        return

    if not head.next:
        return

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    slow2 = head
    while slow.next:
        slow = slow.next
        slow2 = slow2.next

        if slow == slow2:
            return slow

    return

def check_linked_list_is_pallindrome(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    while prev and head:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next

    return True

# ll1 = LinkedList.insert_values([1,2,3,3,2])
# new_list = check_linked_list_is_pallindrome(ll1)
# print(new_list)

def get_kth(head, k):
    while head and k > 0:
        head = head.next
        k -= 1
    return head

def reverse_linked_list_in_group_k(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next
        prev, curr = kth.next, group_prev.next

        while curr != group_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp

    return dummy.next

# ll1 = LinkedList.insert_values([1,2,3,4,5,6,7])
# out = reverse_linked_list_in_group_k(ll1, 3)
# LinkedList.print_ll(out)

def find_intersection_point_of_y_linkedlist(head1, head2):
    list1 = head1
    list2 = head2

    while list1 != list2:
        list1 = list1.next if list1 else head2
        list2 = list2.next if list2 else head1

    return list1

l1 = ListNode(1,None)
l2 = ListNode(2, l1)
l3 = ListNode(3, l2)
l4 = ListNode(4, l3)
l5 = ListNode(5, l4)
l6 = ListNode(6, l5)
first_head = ListNode(7, l6)

il1 = ListNode(11, None)
il2 = ListNode(12, il1)
il3 = ListNode(13, il2)
il4 = ListNode(14, il3)
second_head = ListNode(15, il4)

# il4 = LinkedList.merge_two_linked_lists(second_head, l4)
# ll = find_intersection_point_of_y_linkedlist(first_head, second_head)
# LinkedList.print_ll(ll)

def permutations(nums):
    result = []
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutations(nums)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)

    return result

print(permutations([1,2,3]))