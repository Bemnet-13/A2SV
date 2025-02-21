# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * n

        for first, last, capacity in bookings:
            seats[first - 1] += capacity
            if last < n:
                seats[last] -= capacity
        
        for i in range(1, n):
            seats[i] += seats[i - 1]
        
        return seats