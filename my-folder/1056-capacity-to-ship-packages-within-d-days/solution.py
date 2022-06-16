class Solution:
    def isFeasible(self, weights, capacity, given_days):
    
        days = 1
        curr_wt = 0
        for w in weights:
            curr_wt += w
            if curr_wt > capacity:
                days += 1
                curr_wt = w
        return days <= given_days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        arr = list(range(max(weights), sum(weights)+1))
        left = 0
        right = len(arr)-1

        while left < right:
            mid = (left + right)//2
            if self.isFeasible(weights, arr[mid], days):
                right = mid
            else:
                left = mid + 1

        if self.isFeasible(weights, arr[left], days):
            return arr[left]

        return 0
