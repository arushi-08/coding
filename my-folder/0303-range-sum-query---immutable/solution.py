class NumArray:

    def __init__(self, nums: List[int]):
        # handle multiple queries
        # calculate sum between left and right inclusive
        self.nums = nums
        self.psum = [0]
        for i in range(len(nums)):
            self.psum.append(nums[i] + self.psum[-1])

        # 0,-2,-2,1

    def sumRange(self, left: int, right: int) -> int:
        
        # 0,2
        # -2+0+3
        return self.psum[right+1] - self.psum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
