# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # If the root is None
        # TODO
        ans = []
        level = 0
        queue = deque([(root, level)])
        while queue:
            curr_level = []
            while queue and queue[0][1] == level:
                lastPopped = queue.popleft()[0]
                if lastPopped:
                    curr_level.append(lastPopped.val)
                    queue.append((lastPopped.left, level + 1))
                    queue.append((lastPopped.right, level + 1))
            if curr_level:
                ans.append(curr_level)
            level += 1

        return ans