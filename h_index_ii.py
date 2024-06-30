class Solution:
    def hIndex(self, citations) -> int:
        n = len(citations)
        r = n
        l = 0

        while l < r:
            mid = (l + r) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid
        return n - l