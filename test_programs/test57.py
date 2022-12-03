
def n_meetings_in_a_room(start_times, end_times):
    meetings = []
    allowed_meetings = []
    for i in range(len(start_times)):
        meetings.append((start_times[i], end_times[i], i + 1))

    meetings.sort(key = lambda i: i[1])
    allowed_meetings.append(meetings[0][2])
    end_time = meetings[0][1]
    
    for i in range(1, len(meetings)):
        if end_time < meetings[i][0]:
            allowed_meetings.append(meetings[i][2])
            end_time = meetings[i][1]

    return allowed_meetings

# start_list = [1,3,0,5,8,5]
# end_list = [2,4,6,7,9,9]
# print(n_meetings_in_a_room(start_list, end_list))

def max_consecutive_1s(nums):
    count = 0
    max_count = 0
    for i in range(1, len(nums)):
        if nums[i] == 1:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0

    return max_count

# print(max_consecutive_1s([1,1,1,0,0,0,1,1,0,2,3,4,6,1,1,1,1,1,1]))

def remove_duplicate_from_sorted_array(nums):
    left, right = 1, 1

    while right < len(nums):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
        right += 1
    return left


# nums = [1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
# print(remove_duplicate_from_sorted_array(nums))

def trapping_rainwater(nums):
    if not nums:
        return 0

    left, right = 0, len(nums) - 1
    max_left = nums[left]
    max_right = nums[right]
    res = 0

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, nums[left])
            res += max_left - nums[left]
        else:
            right -= 1
            max_right = max(max_right, nums[right])
            res += max_right - nums[right]

    return res

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapping_rainwater(heights))
    
