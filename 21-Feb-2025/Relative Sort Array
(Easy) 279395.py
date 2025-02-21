# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sorted_arr = []
        extra = []
        counter = defaultdict(int)
        common = set(arr2)

        for num in arr1:
            counter[num] += 1
            if num not in common:
                extra.append(num)
        extra.sort()
        for elem in arr2:
            sorted_arr.extend([elem] * counter[elem])
        sorted_arr.extend(extra)
        return sorted_arr