# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        sorted_arr = sorted(list(counter.items()), key = lambda x:x[1], reverse = True)

        ans = []

        for key, freq in sorted_arr:
            ans.append(key * freq)
        
        return "".join(ans)