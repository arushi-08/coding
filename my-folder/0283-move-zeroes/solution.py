class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # algo: slow ptr and i if i != 0: swap slow ptr and i
        # 0 1 0 3 12 swap 1 0
        ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
             
