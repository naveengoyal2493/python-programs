

from tabnanny import check


def merge_sort(nums):
    mid = len(nums) // 2
    if len(nums) > 1:
        left_array = nums[:mid]
        right_array = nums[mid:]
    
        merge_sort(left_array)
        merge_sort(right_array)

        lind, rind, n = 0, 0, 0
        while lind < len(left_array) and rind < len(right_array):
            if left_array[lind] < right_array[rind]:
                nums[n] = left_array[lind]
                lind += 1
            else:
                nums[n] = right_array[rind]
                rind += 1
            n += 1

        while lind < len(left_array):
            nums[n] = left_array[lind]
            lind += 1
            n += 1

        while rind < len(right_array):
            nums[n] = right_array[rind]
            rind += 1
            n += 1

    return nums

print(merge_sort([4,2,5,7,8,1,2,4,5,6]))



def check_pallindrome(string, left, right):
    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    else:
        left += 1
        right -= 1
        check_pallindrome(string, left, right)


print(check_pallindrome("ala", 0 , 2))