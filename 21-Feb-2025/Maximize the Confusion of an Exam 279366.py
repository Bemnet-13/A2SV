# Problem: Maximize the Confusion of an Exam - https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counter = defaultdict(int)
        max_consecutive = 0

        l = r = 0
        while r < len(answerKey):
            # Logic: If the current letter in answerKey is the dominant letter 
            # and the non-dominant letter has a frequency letter <= k, then add r++
            # If the current letter is not the dominant letter and its frequency is 
            # less than k, then r++
            # If the current letter is not dominant and its frequency is == k then 
            # l++
            currentLetter = answerKey[r]
            inverse = self.inverseLetter(currentLetter)
            if counter[currentLetter] >= counter[inverse] and counter[inverse] <= k:
                counter[answerKey[r]] += 1
                r += 1
            elif counter[currentLetter] < counter[inverse] and counter[currentLetter] < k:
                counter[answerKey[r]] += 1
                r += 1
            elif counter[currentLetter] < counter[inverse] and counter[currentLetter] == k:
                counter[answerKey[l]] -= 1
                l += 1
            
            max_consecutive = max(max_consecutive, counter['F'] + counter['T'])
        
        return max_consecutive
    
    def inverseLetter(self, letter):
        return 'F' if letter == 'T' else 'T'