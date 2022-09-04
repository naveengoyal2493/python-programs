
# Time Comlexity O(n)
# Space Complexity O(n)
def find_repeating_and_missing_numbers_with_On_space(nums):
    new_array = [False] * (len(nums) + 1)
    for i in range(len(nums)):
        if new_array[nums[i]]:
            duplicate = nums[i]
        new_array[nums[i]] = True

    for j in range(1, len(new_array)):
        if not new_array[j]:
            missing = j

    return duplicate, missing

# print(find_repeating_and_missing_numbers_with_On_space([1,2,2,4]))
        
# Time Comlexity O(n)
# Space Complexity O(1)
def find_repeating_and_missing_numbers_with_O1_space(nums): 
    # code here
    for i in range(len(nums)):
        x = abs(nums[i]) - 1
        if nums[x] < 0:
            repeating = x + 1
        else:
            nums[x] = -nums[x]
    
    for i in range(len(nums)):
        if nums[i] > 0:
            missing = i + 1
            break

    return (repeating, missing)
        

print(find_repeating_and_missing_numbers_with_O1_space([1,1,5,4,3]))
    

