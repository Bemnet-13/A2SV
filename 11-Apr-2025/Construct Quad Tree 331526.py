# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isLeaf(row1, col1, row2, col2):
            check = grid[row1][col1]
            for i in range(row1, row2 + 1):
                for j in range(col1, col2 + 1):
                    if grid[i][j] != check:
                        return False, grid[i][j]
            
            return True, check

        def constructQuadTree(row1, col1, row2, col2):
            is_node_leaf, val = isLeaf(row1, col1, row2, col2)
            if is_node_leaf:
                return Node(val, True, None, None, None, None)
            

            new_node = Node(val, False, None, None, None, None)
            
            mid_row = (row1 + row2) // 2
            mid_col = (col1 + col2) // 2
            new_node.topLeft = constructQuadTree(row1, col1, mid_row,  mid_col)
            new_node.topRight = constructQuadTree(row1, mid_col + 1, mid_row,  col2)
            new_node.bottomLeft = constructQuadTree(mid_row + 1, col1, row2, mid_col)
            new_node.bottomRight = constructQuadTree(mid_row + 1, mid_col + 1, row2, col2)

            return new_node
        
        n = len(grid)
        return constructQuadTree(0, 0, n - 1, n - 1)
