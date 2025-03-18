# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def inorder(node, curr_sum):
            if not node:
                return
            if node and not node.left and not node.right:
                curr_sum = curr_sum * 10 + node.val
                self.ans += curr_sum
                return
            
            curr_sum = curr_sum * 10 + node.val
            inorder(node.left, curr_sum)
            inorder(node.right, curr_sum)
        
        inorder(root, 0)
        return self.ans
