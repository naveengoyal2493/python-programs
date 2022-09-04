
class Solution:
    def swap(self, nums, ind1, ind2):
        temp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = temp
        return nums

    def reverse_numbers(self, nums, beg, end):
        while beg < end:
            nums = self.swap(nums, beg, end)
            beg += 1
            end -= 1
        return nums


    def nextPermutation(self, nums: list[int]) -> None:
        if len(nums) == 1:
            return
        if len(nums) == 2:
            return self.swap(nums, 0, 1)
        dec = len(nums) - 2
        while nums[dec] >= nums[dec + 1] and dec >= 0:
            dec -= 1
        nums = self.reverse_numbers(nums, dec + 1, len(nums) - 1)
        if dec == -1:
            return
        next_index = dec + 1
        while nums[dec] >= nums[next_index] and next_index < len(nums):
            next_index += 1
        nums = self.swap(nums, next_index, dec)

