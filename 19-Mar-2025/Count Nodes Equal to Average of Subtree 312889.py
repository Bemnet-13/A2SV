# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def averageCalc(node):
            nonlocal ans
            if node is None:
                return 0, 0
            
            left_nodes, left_sum = averageCalc(node.left)
            right_nodes, right_sum = averageCalc(node.right)

            average = (node.val + left_sum + right_sum) // (1 + left_nodes + right_nodes)
            if average == node.val:
                ans += 1
            return (1 + left_nodes + right_nodes), (node.val + left_sum + right_sum)
        
        averageCalc(root)
        return ans