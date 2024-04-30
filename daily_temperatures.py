class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        answer = [0] * len(temperatures)
        p = 0

        for i in range(len(temperatures)):
            temp = temperatures[i]
            if stack == []:
                stack.append(temp)
            else:
                k = i - 1
                while stack and stack[-1] < temp:
                    if answer[k] != 0:
                        k -= 1
                        continue
                    last = stack.pop()
                    answer[k] = i - k
                    k -= 1
                stack.append(temp)

        return answer