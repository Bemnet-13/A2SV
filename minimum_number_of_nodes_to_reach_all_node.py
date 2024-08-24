class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        startEdges = set()
        destinationEdges = set()
        for from_, to in edges:
            startEdges.add(from_)
            destinationEdges.add(to)
        
        return list(startEdges - destinationEdges)
        