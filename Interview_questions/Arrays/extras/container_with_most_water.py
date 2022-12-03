def find_max_water(nums):
    left = 0
    right = len(nums) - 1
    max_water = 0

    while left < right:
        min_height = min(nums[left], nums[right])
        gap = right - left
        water_contained = min_height * gap
        max_water = max(max_water, water_contained)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return max_water

height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
height = []
print(find_max_water(height))