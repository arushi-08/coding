class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        # select 2 smallest int
        # remove them
        # insert min(x,y)*2 + max(x,y)
        # return min ops so that all elements are >= k

        min_ops = 0
        heapify(nums)

        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, 2*x + y)
            min_ops += 1
        
        return min_ops

