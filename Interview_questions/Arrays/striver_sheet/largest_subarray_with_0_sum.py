def largest_subarray_with_0_sum(nums):
    hash_map = {0:0}
    total_sum = 0
    max_length = 0

    for i in range(len(nums)):
        total_sum += nums[i]
        if total_sum not in hash_map:
            hash_map[total_sum] = i + 1
        else:
            total_length = i - hash_map[total_sum] + 1
            max_length = max(total_length, max_length)
    
    return max_length

print(largest_subarray_with_0_sum([2,8,-3,-5,2,-4,6,1,2,1,-3,4]))