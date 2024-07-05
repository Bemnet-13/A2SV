class Solution:
    def topKFrequent(self, nums, k: int):
        store = {}
        for i in nums:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1
        
        frequencies = list(store.items())
        frequencies.sort(key = lambda i : i[1], reverse= True)

        k_top = []
        for n in range(len(frequencies)):
            if len(k_top) < k:
                k_top.append(frequencies[n][0])
            else:
                break
        
        return k_top
        
trial = Solution()
o = trial.topKFrequent(nums = [2,2,1,1,1,1,1,3], k = 2)
print(o)