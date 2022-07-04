import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for idx, coord in enumerate(points):
            x, y = coord
            heapq.heappush(heap, (math.sqrt(pow(x,2) + pow(y,2)), coord))
        
        ans = []
        while k > 0:
            _, coord = heapq.heappop(heap)
            ans.append(coord)
            k -= 1
            
        return ans
