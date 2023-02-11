"""
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 

Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 

Example 2:

Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output:
160.00
Explanation:
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.
"""

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        

def fractional_knapsack_problem(W: int, arr: list[Item], n):
    new_list = []
    for item in arr:
        unit_weight = (item.value * 1.0) / (item.weight * 1.0)
        new_list.append((item.value, item.weight, unit_weight))

    new_list.sort(key = lambda x: x[2], reverse=True)
    max_val = 0
    new_weight = 0
    for item in new_list:
        if new_weight + item[1] < W:
            max_val += item[0]
            new_weight += item[1]
        else:
            x = (W-new_weight)* 1.0
            max_val += (x*item[2])
            break

    return max_val

n = 84
w = 87
values = [78, 94, 87, 50, 63, 91, 64, 41, 73, 12, 68, 83, 63, 68, 30, 23, 70, 94, 12, 30, 22, 85, 99, 16, 14, 92, 57, 63, 97, 6, 85, 37, 47, 14, 25, 83, 15, 35, 44, 88, 77, 89, 4, 55, 33, 77, 40, 27, 95, 96, 35, 68, 98, 18, 53, 2, 87, 66, 45, 41, 32, 98, 82, 10, 68, 98, 87, 7, 20, 29, 33, 4, 71, 9, 41, 97, 19, 47, 22, 80, 65, 42, 94, 35]
weight = [16, 36, 43, 22, 28, 10, 27, 27, 37, 19, 30, 31, 24, 36, 3, 9, 18, 7, 43, 24, 20, 38, 25, 21, 27, 31, 24, 21, 32, 26, 28, 6, 30, 8, 46, 46, 18, 15, 1, 9, 29, 35, 2, 50, 11, 19, 13, 37, 40, 21, 29, 2, 3, 43, 7, 31, 42, 40, 20, 30, 18, 22, 26, 28, 7, 4, 16, 34, 25, 22, 30, 20, 19, 16, 50, 24, 46, 2, 6, 39, 29, 1, 1, 15]
arr = []
for i in range(n):
    arr.append(Item(values[i], weight[i]))

print(fractional_knapsack_problem(w, arr, n))


