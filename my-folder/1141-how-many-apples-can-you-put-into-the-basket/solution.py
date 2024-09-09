class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        limit = 5000
        
        if sum(weight) <= limit:
            return len(weight)
        
        weight.sort()
        
        curr_wt = 0
        count = 0
        for wt in weight:
            if curr_wt + wt <= limit:
                curr_wt += wt
                count += 1
            else:
                return count
        
        return count
