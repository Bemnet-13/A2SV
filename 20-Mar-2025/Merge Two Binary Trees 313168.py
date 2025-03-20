# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merger(node1, node2):
            if not node1:
                return node2
            if not node2:
                return node1
            
            new_node = TreeNode(node1.val + node2.val)
            new_node.left = merger(node1.left, node2.left)
            new_node.right = merger(node1.right, node2.right)
            return new_node
        
        return merger(root1, root2)

            