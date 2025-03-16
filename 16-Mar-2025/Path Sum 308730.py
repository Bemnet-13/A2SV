# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def inorder(node, score):
            if not node:
                return False
            
            if node and not node.left and not node.right:
                return score + node.val == targetSum
            
            return inorder(node.left, score + node.val) or inorder(node.right, score + node.val)
            
        return bool(root) and inorder(root, 0)