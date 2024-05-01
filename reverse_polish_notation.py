import math
class Solution:
    def evalRPN(self, tokens) -> int:
        # Inititalize operators called set 
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                if token == '+':
                    res = int(operand_2) + int(operand_1)
                    stack.append(str(res))
                elif token == '-':
                    res = int(operand_2) - int(operand_1)
                    stack.append(str(res))
                elif token == '*':
                    res = int(operand_2) * int(operand_1)
                    stack.append(str(res))
                else:
                    res = int(operand_2) / int(operand_1)
                    if res < 0:
                        res = math.ceil(res)
                    else:
                        res = math.floor(res)
                    stack.append(str(res))
        return int(stack[-1])
    
trial = Solution()
o = trial.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(o)