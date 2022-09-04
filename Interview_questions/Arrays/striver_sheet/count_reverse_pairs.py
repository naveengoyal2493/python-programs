# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

class Solution:
    def reversePairs(self, nums):
        self.count = 0
        self.merge_sort(nums)
        return self.count


    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left_array = nums[:mid]
            right_array = nums[mid:]

            self.merge_sort(left_array)
            self.merge_sort(right_array)

            i,j= 0,0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] > 2 * right_array[j]:
                    self.count += len(left_array) - i
                    i += 1
                else:
                    j += 1

            i,j,k = 0,0,0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    nums[k] = left_array[i]
                    i += 1
                else:
                    nums[k] = right_array[j]
                    j += 1
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

print(Solution().reversePairs([2,4,3,5,1]))
