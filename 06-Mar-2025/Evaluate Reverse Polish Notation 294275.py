# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        stack = []
        ops = {'+', '-', '*', '/'}

        for o in tokens:
            if o not in ops:
                stack.append(int(o))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                res = self.calculator(o, op1, op2)
                stack.append(res)
        
        return stack[-1]
    
    def calculator(self, operator, op1, op2):
        if operator == "+": return op1 + op2
        elif operator == "-": return op1 - op2
        elif operator == "*": return op1 * op2
        else: return int(op1 / op2)