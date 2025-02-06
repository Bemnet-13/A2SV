import math
class Solution:
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        
        clone = x

        digits = int(math.log10(x))
        sum_ = 0

        while digits >= 0:
            rem = clone % 10
            sum_ += rem * 10 ** digits
            digits -= 1
            clone = clone // 10
        
        return x == sum_

print(isPalindrome(222))