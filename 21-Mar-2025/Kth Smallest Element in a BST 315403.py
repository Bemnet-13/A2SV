# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr_k = 0
        ans = -1

        def inorder(node):
            nonlocal curr_k
            nonlocal ans
            if not node:
                return
            
            inorder(node.left)
            curr_k += 1
            if curr_k == k:
                ans = node.val
                
            inorder(node.right)
        inorder(root)
        return ans