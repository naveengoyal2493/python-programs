def subset_sums(nums):
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(sum(subset))
            return

        subset.append(nums[i])
        dfs(i + 1)

        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res
        
print(subset_sums([1,2,3]))