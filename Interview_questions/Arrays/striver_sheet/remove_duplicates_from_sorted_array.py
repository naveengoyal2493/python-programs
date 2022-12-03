def remove_duplicates(nums):
    left, right = 1, 1
    while right < len(nums):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
        right += 1
    return nums

nums = [1,2,1,1,3,4,2,3]
print(remove_duplicates(nums))