import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """put everything in max heap and return kth - O(Nlogk) or O(N+logk)
            use min heap put k, last return 1st element
        """
        
        heap = []
        for idx, val in enumerate(nums):
            if len(heap) >= k:
                heapq.heappushpop(heap, val)
            else:
                heapq.heappush(heap, val)
        
        return heapq.heappop(heap)
        
        
        
