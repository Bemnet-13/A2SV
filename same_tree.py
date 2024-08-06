# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        if p is None and q is None:
            return True
        elif not (p and q):
            return False
        elif p.val != q.val:
            return False
        res1 = self.isSameTree(p.left, q.left)
        res2 = self.isSameTree(p.right, q.right)
        return res1 and res2