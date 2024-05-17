from random import random
class Solution:

    def __init__(self, w: List[int]):
        self.psum = []
        self.total_sum = 0
        for i in range(len(w)):
            self.total_sum += w[i]
            self.psum.append(self.total_sum)
            

    def pickIndex(self) -> int:
        rand_val = self.total_sum * random()
        start, end = 0, len(self.psum)-1
        idx = end
        while start <= end:
            mid = (start + end)//2
            if self.psum[mid] >= rand_val:
                idx = min(idx, mid)
                end = mid - 1
            else:
                start = mid + 1
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
