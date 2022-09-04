class Solution:
    def findTarget(self, root, k: int):
        def sorted_list(root):
            elements = []
            if root.left:
                elements += sorted_list(root.left)
            elements.append(root.val)
            if root.right:
                elements += sorted_list(root.right)
            return elements
        
        elements = sorted_list(root)
        left = 0
        right = len(elements) - 1
        for num in elements:
            if left > right:
                return False
            total_sum = elements[left] + elements[right]
            if total_sum == k:
                return True
            elif total_sum < k:
                right = right - 1
            else:
                left = left + 1