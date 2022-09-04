from logging import root
import re


def stocks_buy_and_sell(prices):
    left, right = 0, 1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit


def maximum_subarray_sum(nums):
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(curr_sum, max_sum)
    return max_sum

def swap(nums, ind1, ind2):
    temp = nums[ind1]
    nums[ind1] = nums[ind2]
    nums[ind2] = temp
    return nums

def sort_array(nums):
    left, right = 0, len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            swap(nums, left, i)
            left += 1
        elif nums[i] == 2:
            swap(nums, i, right)
            right -= 1
            i -= 1
        i += 1
    return nums

# print(sort_array([0,1,1,0,2,1,0,2,2,1,0,1]))

def pascals_triangle(n):
    res = [[1]]
    for _ in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res

print(pascals_triangle(5))


