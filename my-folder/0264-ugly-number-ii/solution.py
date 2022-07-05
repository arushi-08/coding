from heapq import heappush, heappop
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        result = []
        heap = [1]
        seen = {1}
        while len(result) < n:
            curr = heappop(heap)
            result.append(curr)
            for m in [2,3,5]:
                if curr * m not in seen:
                    seen.add(curr*m)
                    heappush(heap, curr*m)
        
        return result[-1]
