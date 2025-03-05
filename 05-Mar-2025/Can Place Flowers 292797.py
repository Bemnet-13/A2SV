# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = len(flowerbed)
        
        valid = 0
        i = 0

        while i < k:
            if i == 0 and i == k - 1 and flowerbed[i] == 0:
                valid += 1
            elif i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                i += 1
                valid += 1
            elif i == k - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                i += 1
                valid += 1
            else:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    i += 1
                    valid += 1
            i += 1
        
        if valid >= n:
            return True
        return False