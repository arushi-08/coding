class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        ones = iter(i for i,seat in enumerate(seats) if seat)
        prev = front_zeros = next(ones)
        mid_zeros = 0
        for i in ones:
            mid_zeros = max(mid_zeros, i - prev - 1)
            prev = i
        
        rear_zeros = len(seats) - prev - 1
        
        return max(front_zeros, (mid_zeros + 1) >> 1, rear_zeros)
                
