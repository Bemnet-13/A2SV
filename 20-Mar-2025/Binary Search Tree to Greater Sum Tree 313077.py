# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = 0
        def traverse(node):
            nonlocal ans
            if not node:
                return None
            
            traverse(node.right)
            node.val = node.val + ans
            ans = node.val
            traverse(node.left)
            return node

        return traverse(root)
