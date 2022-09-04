class Solution:

    def swap_numbers(self, nums, ind1, ind2):
        temp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = temp

        return nums

    def reverse_numbers(self, nums, beg, end):
        while beg < end:
            nums = self.swap_numbers(nums, beg, end)
            beg += 1
            end -= 1
        return nums
    
    def nextPermutation(self, nums):
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            return self.swap_numbers(nums, 0, 1)
        dec = len(nums) - 2
        while nums[dec] >= nums[dec + 1] and dec >= 0:
            dec -= 1
        self.reverse_numbers(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return nums
        next_num = dec + 1
        while next_num < len(nums) and nums[next_num] <= nums[dec]:
            next_num += 1
        self.swap_numbers(nums, next_num, dec)
        return nums


print(Solution().nextPermutation([1,5,4,3,2]))

