# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        def validateBST(node):
            nonlocal ans
            if node and not node.left and not node.right:
                return node.val, node.val

            if not node:
                return None, None
            
            # Handle early termination logic
            
            left_min, left_max = validateBST(node.left)
            right_min, right_max = validateBST(node.right)

            if (left_max is not None and left_max >= node.val) or (right_min is not None and right_min <= node.val):
                ans = False

            if left_max is None and right_min and right_min <= node.val:
                ans = False
            
            if right_min is None and left_max and left_max >= node.val:
                ans = False

            if left_min is None:
                left_min = node.val
            if right_max is None:
                right_max = node.val

            return left_min, right_max
        validateBST(root)
        return ans