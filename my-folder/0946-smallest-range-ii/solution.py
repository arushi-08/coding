class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 1: return 0

        nums.sort()

        # find pivot where all values before pivot need to + k
        # and all values at and after pivot need to be - k
        # if we increase all values before mid
        #       then min_val = min(nums[0] + k, nums[mid] - k)
        #       max_val = max(nums[-1] - k, nums[i-1] + k)
        #       store min(max_val - min_val)
        
        high = nums[-1]
        low = nums[0]
        ans = high - low

        for i in range(len(nums)-1):
            min_val = min(low + k, nums[i+1] - k)
            max_val = max(high - k, nums[i] + k)
            ans = min(ans, max_val - min_val)
        
        return ans
                



