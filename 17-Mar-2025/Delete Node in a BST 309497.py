# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Find the inorder successor 
    def minValue(self, node):
        node = node.left
        while node.right:
            node = node.right
        
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            temp = self.minValue(root)
            root.val = temp.val
            root.left = self.deleteNode(root.left, temp.val)
        
        return root
