from heapq import heappush, heappop, heapify, heappushpop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # self.nums = nums
        self.nums = []
        for i in range(len(nums)):
            if not self.nums or k > len(self.nums):
                heappush(self.nums, nums[i])
            elif  k <= len(self.nums) and nums[i] > self.nums[0]:
                heappushpop(self.nums, nums[i])

    def add(self, val: int) -> int:
        if not self.nums or len(self.nums) < self.k:
            heappush(self.nums, val)
            return self.nums[0]
        
        if val < self.nums[0]:
            return self.nums[0]
        heappushpop(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
