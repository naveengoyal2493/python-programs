class Solution:

    def swap(self, nums, ind1, ind2):
        temp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = temp

    def sortColors(self, nums):
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                self.swap(nums, left, i)
                left += 1
            if nums[i] == 2:
                self.swap(nums, i, right)
                right -= 1
                i -= 1
            i += 1
        return nums

print(Solution().sortColors([2,0,2,1,1,0]))
