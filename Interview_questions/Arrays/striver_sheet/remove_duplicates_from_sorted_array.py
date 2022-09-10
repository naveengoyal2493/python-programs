def remove_duplicates(nums):
    left, right = 1, 1
    while right < len(nums):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
        right += 1
    return left

# nums = [1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
# print(remove_duplicates(nums))