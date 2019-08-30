# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None

        v = max(nums)
        
        maxIdx = nums.index(v)
        
        left = self.constructMaximumBinaryTree(nums[:maxIdx])
        right = self.constructMaximumBinaryTree(nums[maxIdx+1:])
        
        root = TreeNode(v)
        root.left = left
        root.right = right
        return root
