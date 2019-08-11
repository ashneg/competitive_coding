class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int,s = 0) -> int:
        if not root:
            return 0
        s = 0
        if root.val >= L and root.val <= R:
            s += root.val
        if root.val > L:
            s += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            s += self.rangeSumBST(root.right, L, R)
        return s
