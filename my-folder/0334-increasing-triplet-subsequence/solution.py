from bisect import bisect_left
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        tail_dp = []
        for i in range(len(nums)):
            idx = bisect_left(tail_dp, nums[i])
            if idx == len(tail_dp):
                tail_dp.append(nums[i])
            else:
                tail_dp[idx] = nums[i]
            if len(tail_dp) >= 3:
                return True
        return False
            
        
        
