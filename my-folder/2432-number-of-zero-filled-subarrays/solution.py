class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        # 10^5 N2 => 10^10 not possible, Nlogn
        
        ans = nums.count(0)
        
        if ans == 0: return ans
        
        res = 0
        
        i = 0 
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                    i += 1

            j = i
            while j < len(nums) and nums[j] == 0:
                j += 1

            num_zeros = len(nums[i:j]) # are zeros 0. 0  0

            res += (num_zeros * (num_zeros + 1)) // 2

            i = j
        
        return res
        
