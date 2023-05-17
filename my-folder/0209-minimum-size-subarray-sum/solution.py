class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 2 pointers + hmap
        # end move to len(nums)
        # if subarrsum >= target: save sublen sum, increase start counter

        subarr_len = len(nums) + 1
        start, end = 0, 0
        subarr_sum = 0
        while end < len(nums):
            subarr_sum += nums[end]
            while subarr_sum >= target:
                subarr_len = min(subarr_len, end-start+1)
                subarr_sum -= nums[start]
                start += 1
            end += 1
        
        if subarr_len == len(nums) + 1:
            return 0
        return subarr_len
