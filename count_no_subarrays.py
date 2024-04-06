class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        # To have an initial window string from index 0 upto k-1
        # we are going to expand the window till we get k odd numbers
        store = {'odd':0 }
        for i in range(k-1):
            if nums[i] % 2 == 1:
                store["odd"] += 1
        
        pointer = k-1
        count = 0
        left = 0
        while pointer < len(nums):
            if nums[pointer] % 2 == 1:
                store["odd"] += 1
            if store["odd"] == k:
                count += 1      
                if nums[left] % 2 == 1:
                    store["odd"] -= 1
                    left += 1
                    continue
            

            pointer += 1
        
        return count
    
trial = Solution()
o = trial.numberOfSubarrays(nums = [1,1,2,1,1], k = 3)
print(o)
            