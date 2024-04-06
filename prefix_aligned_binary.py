
class Solution:
    def numTimesAllBlue(self, flips) -> int:
        count = total = 0
        max_ = 0
        for num in flips:
            total += num
            max_ = max(max_, num)
            if (max_*(max_+1)) // 2 == total:
                count += 1
        return count
   
        # My Own solution with time limit exceeded
        # largest_bit = 0
        # count = 0
        # for i, bit in enumerate(flips, 1):
        #     largest_bit = max(largest_bit, bit)
        #     if largest_bit == i:
        #         count += 1
        # return count

trial =Solution()
o = trial.numTimesAllBlue(flips = [3,2,4,1,5]) 
print(o)