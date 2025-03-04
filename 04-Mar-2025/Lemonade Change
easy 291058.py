# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
                continue
            if bill == 10:
                tens += 1
            else:
                if tens > 0:
                    tens -= 1
                else:
                    fives -= 2
            fives -= 1
        
            if fives < 0:
                return False
        
        return True