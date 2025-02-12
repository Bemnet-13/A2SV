# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {letter : i for i, letter in enumerate(s)}
        anchor = j = 0
        ans = []

        for i, letter in enumerate(s):
            j = max(j, last[letter])

            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        
        return ans