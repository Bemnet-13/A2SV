# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] = arr[i - 1] ^ arr[i]
        
        ans = []
        for left, right in queries:
            curr = arr[right]
            if left - 1 >= 0:
                curr = curr ^ arr[left - 1] 
            ans.append(curr)
        
        return ans