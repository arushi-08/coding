class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:

        usageLimits.sort()
        limit_till_now = 0
        group = 0
        
        for limit in usageLimits:
            limit_till_now += limit

            if limit_till_now >= ((group+1)*(group+2))//2:
                group += 1
        
        return group
