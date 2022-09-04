# O(N^2)
def count_inversions_in_array(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                count += 1

    return count

# print(count_inversions_in_array([3,1,2]))


# O(N.logN)
class Solution:
    def count_inversions(self, nums):
        self.count = 0
        self.merge_sort_2(nums)
        return self.count

    def merge_sort_2(self, nums):
        mid = len(nums) // 2
        if len(nums) > 1:
            left_array = nums[:mid]
            right_array = nums[mid:]

            self.merge_sort_2(left_array)
            self.merge_sort_2(right_array)

            i,j,k = 0,0,0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    nums[k] = left_array[i]
                    i += 1
                else:
                    nums[k] = right_array[j]
                    j += 1
                    self.count += len(left_array) - i
                k += 1

            while i < len(left_array):
                nums[k] = left_array[i]
                i += 1
                k += 1
            
            while j < len(right_array):
                nums[k] = right_array[j]
                j += 1
                k += 1

        return nums

print(Solution().count_inversions([5,4,3,2]))
