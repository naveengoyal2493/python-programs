# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

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

print(three_sum([-1,0,1,2,-1,-4], 0))

