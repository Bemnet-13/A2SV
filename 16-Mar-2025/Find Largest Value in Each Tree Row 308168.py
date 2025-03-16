# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largest = {}

        def preorder(node, level):
            if not node:
                return
            
            if level not in largest:
                largest[level] = node.val
            else:
                largest[level] = max(node.val, largest[level])
            
            preorder(node.left, level + 1)
            preorder(node.right, level + 1)
        
        preorder(root, 0)
        ans = [-1] * len(largest)
        for key, val in largest.items():
            ans[key] = val
        return ans
        
