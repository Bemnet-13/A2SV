from collections import Counter
class Solution:
    def relativeSortArray(self, arr1, arr2):
        count_arr1 = Counter(arr1)
        elements = set(arr1)

        sorted_arr1 = []
        for num in arr2:
            freq = count_arr1[num]
            sorted_arr1.extend([num]*freq)
            del count_arr1[num]
        
        remaining = list(count_arr1.keys())
        remaining.sort()

        for num in remaining:
            freq = count_arr1[num]
            sorted_arr1.extend([num]*freq)
        
        return sorted_arr1
    
trial =Solution()
o = trial.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])
print(o)