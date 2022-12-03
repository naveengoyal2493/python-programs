def remove_duplicates(nums):
    new_list = []

    for num in nums:
        if num not in new_list:
            new_list.append(num)
    
    return new_list

l=[7,7,7,7,2,3,7,7,7,7,7,4,7,8,6,5,4,3,5,7,7,7,7]
print(remove_duplicates(l))
