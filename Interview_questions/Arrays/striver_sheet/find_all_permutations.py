def permutations(nums):
    result = []
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutations(nums)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)

    return result

    
print(permutations([1,2,3]))