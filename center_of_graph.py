class Solution:
    def findCenter(self, edges) -> int:
        edge1, edge2 = edges[0], edges[1]

        for node in edge1:
            if node in edge2:
                return node