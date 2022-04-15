import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        copy = self.nums[:]
        for i in range(0, len(copy)-1):
            j = random.randrange(i, len(copy))
            copy[i] , copy[j] = copy[j] , copy[i]
        
        return copy


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
