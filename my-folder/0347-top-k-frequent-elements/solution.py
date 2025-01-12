import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freq_dict = Counter(nums)
        print('freq_dict', freq_dict)
        for key, val in freq_dict.items():
            if len(heap) == k:
                if val > heap[0][0]:
                    heappop(heap)
                else:
                    continue
            heappush(heap, (val, key))
            
        answer = []
        while heap and k:
            answer.append(heappop(heap)[-1])
            k -= 1
        return answer


