# Given an array nums of n integers, return an array of all the unique quadruplets 
# [nums[a], nums[b], nums[c], nums[d]] such that:

# 1. 0 <= a, b, c, d < n
# 2. a, b, c, and d are distinct.
# 3. nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

class FourSum:

    def four_sum(self, nums, target):
        nums.sort()
        res, quad = [], []
        
        def ksum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    ksum(k-1, i+1, target - nums[i])
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
        ksum(4, 0, target)
        return res

print(FourSum().four_sum([1,0,-1,0,-2,2], 0))