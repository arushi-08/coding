from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        if not s: return ""
        
        s_freq = Counter(s)
        
        heap = []
        for key, val in s_freq.items():
            heappush(heap, (-val, key))
        
        result = ""
        while len(heap) > 1:
            v1, c1 = heappop(heap)
            v2, c2 = heappop(heap)
            result += c1
            # print(result)
            result += c2
            # print(result)
            
            if -v1 > 1:
                heappush(heap, (v1+1, c1))
            if -v2 > 1:
                heappush(heap, (v2+1, c2))
            
        if heap:
            val, char = heap[0]
            # print(val)
            if -val > 1: return ""
            result += char
        
        return result
