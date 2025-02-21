# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        isNegative = True if num < 0 else False
        if isNegative:
            num = abs(num)

        number = list(str(num))
        if isNegative:
            number.sort(reverse = True)
        else:
            number.sort()
            if number[0] =='0':
                i = 0 
                while i < len(number):
                    if number[i] != '0':
                        number[0], number[i] = number[i], number[0]
                        break
                    i += 1
        
        number = int("".join(number))
        return -number if isNegative else number 
