class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        ans = [0] * (n+1)

        for i in range(len(bookings)):
            start, end, seats = bookings[i]

            ans[end] += seats
            if start > 1:
                ans[start - 1]  -= seats
        
        for i in range(len(ans)-2,-1,-1):
            ans[i] += ans[i+1]
        
        return ans[1:]

