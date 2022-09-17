def trapping_rainwater(nums):
    if not nums:
        return 0

    left, right = 0, len(nums) - 1
    max_left, max_right = nums[left], nums[right]
    res = 0

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, nums[left])
            res += max_left - nums[left]
        else:
            right -= 1
            max_right = max(max_right, nums[right])
            res += max_right - nums[right]

    return res

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapping_rainwater(heights))
    