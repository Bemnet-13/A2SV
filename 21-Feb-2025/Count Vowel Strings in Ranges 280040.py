# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ps = []
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                ps.append(1)
            else:
                ps.append(0)
        
        for i in range(1, len(ps)):
            ps[i] += ps[i - 1]
        
        ans = []
        for left, right in queries:
            curr = ps[right]
            if left - 1 >= 0:
                curr -= ps[left - 1]
            ans.append(curr)
        return ans