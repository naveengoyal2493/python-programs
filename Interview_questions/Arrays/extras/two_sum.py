# Given an array of integers nums and an integer target, return indices of the two numbers such 
# that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same 
# element twice.
# You can return the answer in any order.

def find_two_sum(nums, target):
    hash = {}
    for i in range(len(nums)):
        to_find = target - nums[i]
        if to_find in hash:
            return [hash[to_find], i]
        hash[nums[i]] = i

# print(find_two_sum([7,3,4,8,9,1], 8))


def find_two_sum(nums, new_target, target):
    pass

print(find_two_sum([1,2,3],1,3))