# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depthCalculator(node):
            if not node:
                return 0
            
            return 1 + max(depthCalculator(node.left), depthCalculator(node.right))
        
        return depthCalculator(root)