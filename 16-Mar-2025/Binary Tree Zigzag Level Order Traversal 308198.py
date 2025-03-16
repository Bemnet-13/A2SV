# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        def preorder(node, level):
            if not node:
                return
            levels[level].append(node.val)
            preorder(node.left, level + 1)
            preorder(node.right, level + 1)
        
        preorder(root, 0)
        ans = []
        reverse = False
        for i in range(len(levels)):
            l = levels[i]
            if reverse: l = l[::-1]
            ans.append(l)
            reverse = not reverse
        
        return ans