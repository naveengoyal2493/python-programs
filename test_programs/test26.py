class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def makeBST(self,nums,left,right):
        if left >=  right:
            return None
        elif left == right -1:
            return TreeNode(nums[left])
        else:
            mid = (left + right)//2
            leftPart = self.makeBST(nums,left,mid)
            rightPart = self.makeBST(nums,mid+1,right)
            result = TreeNode(nums[mid],leftPart,rightPart)
            return result
            
    def sortedArrayToBST(self, nums):
        return self.makeBST(nums,0,len(nums))

arr = [0,1,2,3,4,5]