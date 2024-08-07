# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case

        if root.val == val:
            return root
        
        if root.left and val < root.val:
            return self.searchBST(root.left, val)
        if root.right and val > root.val:
            return self.searchBST(root.right, val)