# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def post_order(node):
            nonlocal ans
            if not node:
                return
            if node.left:
                post_order(node.left)
            if node.right:
                post_order(node.right)
            ans.append(node.val)
        post_order(root)
        return ans