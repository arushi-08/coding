class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr, p1, p2 = 0, 0, len(nums)-1
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p1] = nums[p1], nums[curr]
                curr += 1
                p1 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
