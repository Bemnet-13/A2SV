class Solution:
    def corpFlightBookings(self, bookings, n: int):
        reserved_seats = [0 for _ in range(n)]

        for first, last, seats in bookings:
            reserved_seats[first - 1] += seats
            if last < n:
                reserved_seats[last] -= seats
        
        for i in range(1, n):
            reserved_seats[i] += reserved_seats[i - 1]
        
        return reserved_seats
    
trial = Solution()
o = trial.corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5)
print(o)
