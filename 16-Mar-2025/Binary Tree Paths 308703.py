# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def preorder(node, path):
            nonlocal ans
            if not node:
                path.append("0")
                return

            path.append(str(node.val))
            if node and not node.left and not node.right:
                ans.append(path[:])
                return
            
            preorder(node.left, path)
            if path:
                path.pop()
            preorder(node.right, path)
            if path:
                path.pop()
                    
        preorder(root, [])
        for i in range(len(ans)):
            ans[i] = "->".join(ans[i])
        
        return ans