class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_og = nums.copy()
        nums.sort()
        largest_num = nums[-1]
        for i in range(len(nums)-1):
            if nums[i]*2 > largest_num:
                return -1
        
        return nums_og.index(largest_num)
