# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #  Using binary Search to find the closest index to x
        start, end = self.findPivotIndex(arr, k, x)
        min_start, min_end = start, end
        print(start, end)

        total_error = 0
        for i in range(min_start, min_end + 1):
            total_error += abs(arr[i] - x)
        print(total_error)
        min_error = total_error
        i = 0
        while end + 1 < len(arr) and i < k + 1:
            total_error -= abs(arr[start] - x)
            total_error += abs(arr[end + 1] - x)
            start, end = start + 1, end + 1
            i += 1
            if total_error < min_error:
                min_error = total_error
                min_start = start
                min_end = end
            print("Here")
        
        return arr[min_start: min_end + 1]

            
    
    def findPivotIndex(self, arr, k, x):
        l, r, req = 0, len(arr) - 1, -1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] == x:
                req = mid
                break
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        print(l)
        # If x is not found in arr, set the found index at l or r
        if req == -1 and l != 0:
            req = l - 1
        elif req == -1:
            req = 0
        
        # Set the initial window 
        if req - k + 1 >= 0:
            start = req - k + 1
        else:
            start = 0
        end = start + k - 1

        return start, end