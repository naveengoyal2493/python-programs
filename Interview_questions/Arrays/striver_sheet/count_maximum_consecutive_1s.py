def count_max_consecutive_1s(nums):
    max_count = 0
    count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0

    return max_count

nums = [1,1,1,0,0,1,1,1,1,1,0]
print(count_max_consecutive_1s(nums))