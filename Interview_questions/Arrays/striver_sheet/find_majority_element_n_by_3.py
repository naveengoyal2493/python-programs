def find_majority_element(nums):
    ans = []
    candidate1 = 0
    candidate2 = 0

    life1 = 0
    life2 = 0

    for i in range(len(nums)):
        if candidate1 == nums[i]:
            life1 += 1
        elif candidate2 == nums[i]:
            life2 += 1
        elif life1 == 0:
            candidate1 = nums[i]
            life1 += 1
        elif life2 == 0:
            candidate2 = nums[i]
            life2 += 1
        else:
            life1 -= 1
            life2 -= 1

    count1 = 0
    count2 = 0
    for i in range(len(nums)):
        if candidate1 == nums[i]:
            count1 += 1
        elif candidate2 == nums[i]:
            count2 += 1
        
    if count1 > len(nums)/3:
        ans.append(candidate1)
    if count2 > len(nums)/3:
        ans.append(candidate2)
    
    return ans

            
print(find_majority_element([0,0,0]))