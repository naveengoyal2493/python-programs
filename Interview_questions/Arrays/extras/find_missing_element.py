def find_missing_element(nums):
    res = len(nums)

    for i in range(len(nums)):
        res +=  i - nums[i]

    return res

print(find_missing_element([3,0,1,4,5,6,7]))