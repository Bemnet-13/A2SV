# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_ = defaultdict(int)
        self.sum_[0] = 1
        self.ans = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def inorder(node, running_sum):
            if not node:
                return
            
            running_sum += node.val
            self.ans += self.sum_[running_sum - targetSum]
            self.sum_[running_sum] += 1

            inorder(node.left, running_sum)
            inorder(node.right, running_sum)
            self.sum_[running_sum] -= 1
        
        inorder(root, 0)
        return self.ans