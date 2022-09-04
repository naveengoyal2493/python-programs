def find_majority_element(nums):
    candidate = 0
    life = 0

    for i in range(len(nums)):
        if candidate == nums[i]:
            life += 1
        elif life == 0:
            candidate = nums[i]
            life += 1
        else:
            life -= 1
    return candidate

print(find_majority_element([2,2,2,2,2,3,3,3,3]))




