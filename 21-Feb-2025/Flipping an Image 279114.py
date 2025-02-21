# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        
        for row in image:
            for left in range(n // 2):
                right = n - 1 - left
                row[left], row[right] = row[right], row[left]
        
        # Inverting
        for row in range(n):
            for col in range(n):
                if image[row][col] == 1:
                    image[row][col] = 0
                else:
                    image[row][col] = 1
        
        return image
