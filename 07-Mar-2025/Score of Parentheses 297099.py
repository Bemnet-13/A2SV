# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        scores, stack = [], []
        init_score = 1
        score = 0
        
        for i, brace in enumerate(s):
            if brace == '(':
                if len(stack) >= 1:
                    scores.append(score * (2**(len(stack))))
                else:
                    scores.append(score)
                score = 0
                stack.append(brace)
            else:
                stack.pop()
                score = 1 if score == 0 else score * 2

        return sum(scores) + score