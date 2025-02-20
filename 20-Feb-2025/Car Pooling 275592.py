# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        destinations = [0] * 1002

        for passengers, from_, to_ in trips:
            destinations[from_ + 1] += passengers
            destinations[to_ + 1] -= passengers



        for i in range(1, len(destinations)):
            destinations[i] += destinations[i - 1]
            if destinations[i] > capacity:
                return False
        
        return True