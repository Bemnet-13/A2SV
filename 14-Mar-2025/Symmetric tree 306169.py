# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def checkSymmetry(left, right):
            if not left and right or not right and left:
                return False
            
            if not left and not right:
                return True
            
            if left.val != right.val:
                return False

            ans1 = checkSymmetry(left.right, right.left)
            ans2 = checkSymmetry(left.left, right.right)
            return ans1 and ans2

        return checkSymmetry(root.left, root.right)