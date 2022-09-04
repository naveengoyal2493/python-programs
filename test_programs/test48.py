
from turtle import right


def two_sum(nums, target):
    hash = {}
    for i, value in enumerate(nums):
        to_find = target - value
        if to_find in hash:
            return [hash[to_find], i]
        hash[value] = i

# nums, target = [7,3,4,8,9,1], 10
# print(two_sum(nums, target))

def two_sum_II(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [left+1, right+1]

# print(two_sum_II([1,3,4,5,7,10,11], 9))

def three_sum(nums, target):
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        a = nums[i]
        while left < right:
            if a + nums[left] + nums[right] < target:
                left += 1
            elif a + nums[left] + nums[right] > target:
                right -= 1
            else:
                pass

