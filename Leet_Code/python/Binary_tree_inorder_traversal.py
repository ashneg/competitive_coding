class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        
        inorder(root)
        return res
