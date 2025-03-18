# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def inorder(node, parent, grandparent):
            nonlocal ans
            if not node:
                return
                
            if grandparent and grandparent.val % 2 == 0:
                ans += node.val
            
            inorder(node.left, node, parent)
            inorder(node.right, node, parent)
        inorder(root, None, None)
        return ans