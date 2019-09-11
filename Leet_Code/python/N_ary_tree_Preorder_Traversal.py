"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root : return None
        ret = [root.val]
        for value in root.children:
            ret += self.preorder(value)
        return ret
