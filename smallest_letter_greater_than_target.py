class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        l = 0
        r = len(letters) - 1

        while l < r:
            mid = (l + r) // 2
            if ord(letters[mid]) > ord(target):
                r = mid
            else:
                l = mid + 1
        if ord(letters[l]) <= ord(target):
            return letters[0]
        return letters[l]
    
trial = Solution()
o = trial.nextGreatestLetter(letters = ["c","f","j"], target = "a")
print(o)