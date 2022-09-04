def find_second_largest_element(nums):
    if len(nums) < 2:
        return -1
    first = second = -2147483648
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == -2147483648:
        return -1
    else:
        return second

print(find_second_largest_element([12, 35, 1, 10, 34, 1]))