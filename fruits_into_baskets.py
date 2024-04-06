class Solution:
    def totalFruit(self, fruits) -> int:
        basket = {}
        max_count = 0
        left = right = 0

        while right < len(fruits):
            if len(basket) <= 2:
                basket[fruits[right]] = 1
                right += 1
                max_count = max(max_count, right - left)
        
        return max_count
    
trial =Solution()
o = trial.totalFruit()
print(o)