# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = Counter()
        max_fruits = 0

        left = 0
        for right in range(len(fruits)):
            counter[fruits[right]] += 1
            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, sum(counter.values()))
        
        return max_fruits