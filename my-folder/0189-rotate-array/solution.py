class Solution:
    def reverse(self, nums, st, ed):
        while st <= ed:
            nums[st], nums[ed] = nums[ed], nums[st]
            st += 1
            ed -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
