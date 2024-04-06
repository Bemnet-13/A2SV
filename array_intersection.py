class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set(nums1) & set(nums2)
        ans = []
        for elem in intersection:
            ans.extend([elem] * min(nums1.count(elem), nums2.count(elem)))
        return ans