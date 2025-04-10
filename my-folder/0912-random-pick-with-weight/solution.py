from itertools import accumulate
class Solution:

    def __init__(self, w: List[int]):
        # 1
        # 2, 3
        self.w = w
        self.psum = list(accumulate(w))

    def pickIndex(self) -> int:
        
        # find leftmost index where i can insert a random number?
        return bisect.bisect_left( 
            self.psum, 
            random.randint(1, self.psum[-1])
        )



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
