# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        destinations = [0] * 1001

        for passengers, from_, to_ in trips:
            destinations[from_] += passengers
            destinations[to_] -= passengers

        for i in range(1, len(destinations)):
            destinations[i] += destinations[i - 1]
        
        for passengers in destinations:
            if passengers > capacity:
                return False
        
        return True