# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from email import header
from typing import List


def three_sum(nums, target):
    combs = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = a + nums[left] + nums[right]
            if three_sum < 0:
                left += 1
            elif three_sum > 0:
                right -= 1
            else:
                combs.append([a, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return combs

# print(three_sum([-1,0,1,2,-1,-4], 0))


class ListNode:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList:

    def add_data_to_beginning(self, data, head = None):
        return ListNode(data, head)

    def add_list_values(self, nums):
        head = None
        for i in range(len(nums) - 1, -1, -1):
            head = ListNode(nums[i], head)
        return head

    def print_ll(self, head):
        if not head:
            return
        itr = head
        start = ""
        while itr:
            start += str(itr.data) + "-->"
            itr = itr.next
        print(start)

    
l1 = LinkedList().add_list_values([1,2,3,4,5,6])
LinkedList().print_ll(l1)
