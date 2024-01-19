import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freq_dict = Counter(nums)
        for key, val in freq_dict.items():
            heap.append((-val, key))
        
        heapq.heapify(heap)
        answer = []
        while k > 0:
            answer.append(heapq.heappop(heap)[-1])
            k -= 1
        return answer


