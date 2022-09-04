
def two_sum(nums, target):
    already = {}
    for i in range(len(nums)):
        to_find = target - nums[i]
        if to_find in already:
            return [already[to_find], i]
        else:
            already[nums[i]] = i

# print(two_sum([7,3,4,8,9,1], 8))

def two_sum_II(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left+1, right+1]

# print(two_sum_II([1,2,3,4,6], 8))

def three_sum(nums):
    nums.sort()
    combs = []

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

# print(three_sum([-1,0,1,2,-1,-4]))