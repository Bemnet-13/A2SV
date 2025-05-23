# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        queue = deque([root])
        while queue:
            next_node = queue.popleft()
            if next_node and next_node.val != val:
                return False
            if next_node:
                queue.append(next_node.left)
                queue.append(next_node.right)
        
        return True