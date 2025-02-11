# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        maxi = len(arr)

        while maxi >= 1:
            index = arr.index(maxi)
            self.flip(arr, index)
            self.flip(arr, maxi - 1)
            ans.extend([index + 1, maxi])
            maxi -= 1
        return ans


    def flip(self, arr, k):
        left = 0
        right = k

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        