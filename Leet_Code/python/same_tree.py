# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.check_everyone( p,q)
    def check_everyone(self, p,q):
        if (not p) and q or ( not q )and p:
            return False
        if q and  p:
            if q.val != p.val:
                return False
        if not p and not q:
            return True
        a = self.check_everyone(p.left,  q.left)
        b = self.check_everyone(p.right, q.right)
        return a and b
