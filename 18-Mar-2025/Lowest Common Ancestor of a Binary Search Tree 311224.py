# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lowest = math.inf
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def search(node):
            if node is p or node is q:
                self.lowest = min(self.lowest, node.val)
                return node
           
            if node.val > p.val and node.val > q.val:
                self.lowest = min(self.lowest, node.val)
                return search(node.left)
            elif node.val < p.val and node.val < q.val:
                self.lowest = min(self.lowest, node.val)
                return search(node.right)
            else:
                self.lowest = min(self.lowest, node.val)
                return node
                
        return search(root)
           