class Solution:
    def validMountainArray(self, arr) -> bool:
        
        max_num = max(arr)
        is_increasing = False

        i = 0
        while i < len(arr):
            if arr[i] == max_num:
                break
            if arr[i] < arr[i + 1]:
                is_increasing = True
            else:
                return False
            i += 1
        is_decreasing = False

        while i < len(arr) - 1:
            if arr[i] > arr[i + 1]:
                is_decreasing = True
            else:
                return False
            i += 1
        
        return is_increasing and is_decreasing

trial = Solution()
o = trial.validMountainArray(arr = [0,3,2,1])
print(o)