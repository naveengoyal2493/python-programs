def subsets_II(nums):
    nums.sort()
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1)

    dfs(0)
    return res

print(subsets_II([1,2,2]))