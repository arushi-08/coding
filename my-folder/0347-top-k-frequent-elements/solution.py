class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # nlogn - sorting
        # nlogn - minheap
        # nlogk - maxheap - store 1st k elems, pop from heap if new elem > heap top

        hmap = Counter(nums)
        heap = []
        for key, val in hmap.items():
            if len(heap) == k:
                if val > heap[0][0]:
                    heappop(heap)
                else:
                    continue
            heappush(heap, (val, key))
        
        ans = []
        while heap:
            _, key = heappop(heap)
            ans.append(key)
        
        return ans
