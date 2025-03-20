# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sum_ = 0
        def traverse(node):
            nonlocal sum_
            if not node:
                return 0
            
            traverse(node.right)
            node.val += sum_
            sum_ = node.val
            traverse(node.left)
            return sum_
        
        traverse(root)
        return root
