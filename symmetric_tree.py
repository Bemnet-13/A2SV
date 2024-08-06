# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetricChecker(left , right):
            if (left and not right) or (right and not left):
                return False
            elif not right and not left:
                return True
            elif left.val != right.val:
                return False
            l = symmetricChecker(left.left, right.right)
            r = symmetricChecker(left.right, right.left)
            
            return l and r
        
        return symmetricChecker(root.left, root.right)