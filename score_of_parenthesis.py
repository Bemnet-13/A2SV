# class Solution:
#     def scoreOfParentheses(self, s: str) -> int:
#         scores = []
#         stack = []
#         init_score = 1/ 2
#         score = init_score
        
#         for i in range(len(s)):
#             brace = s[i]
#             if brace == '(':
#                 if len(stack) >= 1 and score != 1 / 2:
#                     scores.append(int(score * 2**len(stack)))
#                 elif score != 1 / 2:
#                     scores.append(int(score))
#                 score = init_score
#                 stack.append(brace)
#             else:
#                 if stack:
#                     stack.pop()
#                     score *= 2
#             if i == len(s) - 1:
#                 scores.append(int(score))
#                 score = init_score

                

#         return sum(scores)


from collections import deque

s = deque()

print(s)
print(s[0])