class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        if not duration: return 0
        ans = 0
        n = len(timeSeries)
        for i in range(n-1):
            ans += min(timeSeries[i+1] - timeSeries[i], duration)
        
        return ans + duration


            
