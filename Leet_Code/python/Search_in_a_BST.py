# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None:
            return None
        if root.val==val:
            return root
        root.left=self.searchBST(root.left,val)
        root.right=self.searchBST(root.right,val)
        return root.left or root.right
