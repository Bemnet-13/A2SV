# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(arr):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False


        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                return search(matrix[i])
        
        return False