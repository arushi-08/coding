class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 pointers
        # p1 = 0, p2 = n-1, curr = 0
        # if curr <= curr + 1
        # increasing = True
        for i in range(len(nums)):
            if i % 2 == 0:
                if i+1 < len(nums) and nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                if i+1 < len(nums) and nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
