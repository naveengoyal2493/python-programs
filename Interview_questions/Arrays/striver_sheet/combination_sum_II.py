def combination_sum_II(nums, target):
    nums.sort()
    res = []
    subset = []

    def dfs(i, total):
        if total > target:
            return
        
        if i >= len(nums):
            if total == target:
                res.append(subset.copy())
            return

        subset.append(nums[i])
        dfs(i + 1, total + nums[i])

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        subset.pop()
        dfs(i + 1, total)

    dfs(0, 0)
    return res

nums = [10,1,2,7,6,1,5]
target = 8

print(combination_sum_II(nums, target))