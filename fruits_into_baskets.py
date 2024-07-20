class Solution:
    def totalFruit(self, fruits) -> int:
        max_fruits = start = end = 0
        baskets = {}

        if len(fruits) <= 2:
            return len(fruits)

        while end < len(fruits):
            fruit = fruits[end]
            if len(baskets) == 2 and fruit not in baskets:
                baskets[fruits[start]] -= 1
                if baskets[fruits[start]] == 0:
                    del baskets[fruits[start]]
                start += 1
            elif baskets.get(fruit, 0) > 0:
                baskets[fruit] += 1
                end += 1
            elif baskets.get(fruit, 0) == 0:
                baskets[fruit] = 1
                end += 1
            
            max_fruits = max(max_fruits, end - start)

        return max_fruits