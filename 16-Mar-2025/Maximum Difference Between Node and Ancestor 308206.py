# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        score = 0
        def preorder(node, max_, min_):
            nonlocal score
            if not node:
                return
            
            max_ = max(node.val, max_)
            min_ = min(node.val, min_)
            score = max(score, abs(max_ - min_))
            
            preorder(node.left, max_, min_)
            preorder(node.right, max_, min_)

        preorder(root, float('-inf'), float('inf'))
        return score
