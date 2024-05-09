from heapq import heapify, heappop, heappush
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happykids = []
        heapify(happykids)
        for i in range(len(happiness)):
            heappush(happykids, -happiness[i])
        ans = 0
        count = 0
        while k > 0:
            happy = -(heappop(happykids))
            happy = max(happy-count, 0)
            ans += happy
            k -= 1
            count += 1
        
        return ans
