class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.psum = [nums[0]]
        for i in range(1, len(nums)):
            self.psum.append(nums[i] + self.psum[i-1])
        

    def sumRange(self, left: int, right: int) -> int:
        return self.psum[right] - self.psum[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
