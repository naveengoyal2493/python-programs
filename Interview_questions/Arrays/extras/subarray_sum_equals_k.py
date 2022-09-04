from re import sub


def subarray_sum_equals_k(nums, k):
    sub_arrays = []
    numbers = {0:[1, 0]}
    total_sum = 0

    for index, value in enumerate(nums):
        total_sum += value
        if (total_sum - k) not in numbers:
            numbers[total_sum] = [1, index]
        else:
            inner_sub_array = []
            for i in range(numbers[total_sum - k][1] + 1, index + 1):
                inner_sub_array.append(nums[i])
            numbers[total_sum - k] += 1