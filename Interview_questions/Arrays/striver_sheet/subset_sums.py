def subset_sums(nums):
    res = []
    subset = []
    def dfs(i, total):
        if i >= len(nums):
            res.append(total)
            return

        subset.append(nums[i])
        dfs(i + 1, total + nums[i])

        subset.pop()
        dfs(i + 1, total)

    dfs(0, 0)
    return res
        
print(subset_sums([5,2,1]))