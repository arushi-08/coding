from heapq import heappush
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # heap
        
        freq_dict = Counter(s) # O(N)
        heap = []
        # O(NlogN)
        for key, val in freq_dict.items(): # O(N)
            heappush(heap, (-val, key)) # O(logN)
        
        ans = ""
        
        # O(NlogN)
        while heap: # O(N)
            insert_back = []
            for i in range(2):
                if heap:
                    freq, char = heappop(heap) # O(logN)
                    if ans:
                        if ans[-1] == char:
                            return ""
                    ans += char
                    freq = -freq - 1
                    if freq > 0:
                        insert_back.append((-freq, char))
                    
            for element in insert_back:
                heappush(heap, element) # O(logN)
        
        return ans
        
        
