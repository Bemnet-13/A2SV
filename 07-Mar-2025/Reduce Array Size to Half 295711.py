# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        lst = list(counter.items())
        
        lst.sort(key = lambda i : i[1], reverse = True)
        print(lst)
        count = 0
        n = len(arr)

        for i in range(len(lst)):
            count += lst[i][1]
            if count >= n // 2:
                return i + 1