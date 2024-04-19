class Solution:
    def pancakeSort(self, arr):
        # arr is permutation of 1,..., len(arr)
        # Find the largest element in the array
        # Flip it to make it at index 0
        # Flip the entire pancake upto the number to make it at the correct position
        def flip(lst, r):
            l = 0
            while l < r:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
    
        actions = []
        bottom = max(arr)

        while bottom > 0:
            # Find the index of bottom in the array
            k = arr.index(bottom)
            if k == bottom - 1:
                bottom -= 1
            # Check if the bootom is at index 0
            # If it is zero, then append bottom to actions and flip the array till j
            elif k == 0:
                flip(arr, bottom - 1)
                actions.append(bottom)
                bottom -= 1
            else:
                flip(arr, k)
                actions.append(k + 1)
        
        return actions 

        
trial = Solution()
o = trial.pancakeSort(arr = [3,2,4,1])
print(o)