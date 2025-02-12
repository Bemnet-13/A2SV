# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        left = 0
        ans = []
        
        running_counter = Counter()
        for right in range(len(s)):
            running_counter[s[right]] += 1
            difference = counter - running_counter
            is_valid_partition = True
            for letter in difference:
                if running_counter[letter] > 0:
                    is_valid_partition = False
                    break
            
            if is_valid_partition:
                ans.append(right - left + 1)
                left = right + 1
                running_counter = Counter()
            
        
        return ans