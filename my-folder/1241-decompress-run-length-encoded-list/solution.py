class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        ans = []
        for i in range(0, len(nums)-1, 2):
            freq, val = nums[i], nums[i+1]
            ans += [val]*freq
        return ans
