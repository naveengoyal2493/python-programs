def max_consecutive_ones(nums):
    max_ones = 0
    curr_count = 0

    for num in nums:
        if num == 1:
            curr_count += 1
            max_ones = max(max_ones, curr_count)
        else:
            curr_count = 0

    return max_ones           


prices = [1, 1, 0, 1, 1, 1]
print(max_consecutive_ones(prices))