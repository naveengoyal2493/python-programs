"""
Given an array of distinct integers and a target, you have to return the list of all
unique combinations where the chosen numbers sum to target. You may return the 
combinations in any order.

The same number may be chosen from the given array an unlimited number of times. Two 
combinations are unique if the frequency of at least one of the chosen numbers 
is different.

It is guaranteed that the number of unique combinations that sum up to target is 
less than 150 combinations for the given input.

Example 1:

Input: array = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
             7 is a candidate, and 7 = 7.
             These are the only two combinations.


Example 2:

Input: array = [2], target = 1
Output: []
Explaination: No combination is possible.
"""

def combination_sum(nums, target):
    res = []
    subset = []

    def dfs(i, total):
        if total == target:
            res.append(subset.copy())
            return

        if total > target or i >= len(nums):
            return
        
        subset.append(nums[i])
        dfs(i, total + nums[i])
        subset.pop()
        dfs(i + 1, total)

    dfs(0, 0)
    return res

nums = [10,1,2,7,6,5]
target = 8
print(combination_sum(nums, target))