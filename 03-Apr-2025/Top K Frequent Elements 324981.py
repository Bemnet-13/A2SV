# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        buckets = [set() for _ in range(len(nums) + 1)]

        for i in range(len(nums)):
            count[nums[i]] += 1
            num_count = count[nums[i]] - 1
            buckets[num_count + 1].add(nums[i])

            if num_count > 0:
                buckets[num_count].remove(nums[i])
        
        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            if k == 0:
                break
            while len(buckets[i]) > 0 and k > 0:
                popped = buckets[i].pop()
                ans.append(popped)
                k -= 1
        return ans