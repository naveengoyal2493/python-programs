def longest_integer_sequence(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if (num - 1) not in nums_set:
            length = 0
            while (num + length) in nums_set:
                length += 1
            longest = max(length, longest)
    return longest


print(longest_integer_sequence([100, 4, 200, 1, 3, 2]))