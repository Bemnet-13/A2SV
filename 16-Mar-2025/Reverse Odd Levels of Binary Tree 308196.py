# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        odd_levels = defaultdict(list)
        def preorder(node, level):
            if not node:
                return
            
            if level % 2 == 1:
                odd_levels[level].append(node.val)
            
            preorder(node.left, level + 1)
            preorder(node.right, level + 1)
        
        preorder(root, 0)
        for i, nodes in odd_levels.items():
            odd_levels[i] = deque(nodes[::-1])

        def change_levels(node, level):
            if not node:
                return 
            
            if level % 2 == 1:
                node.val = odd_levels[level].popleft()
            
            change_levels(node.left, level + 1)
            change_levels(node.right, level + 1)
        
        change_levels(root, 0)
        return root
