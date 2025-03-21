# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []
        def inorder(node):
            nonlocal nums
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)

        def insert(left, right):
            if left == right:
                return TreeNode(nums[left])
            if left > right:
                return None
            
            half = (left + right) // 2
            new_root = TreeNode(nums[half])
            new_root.left = insert(left, half - 1)
            new_root.right = insert(half + 1, right)
            return new_root

        return insert(0, len(nums) - 1)