class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 0
        l = 0
        r = 0
        n_jumps = 0
        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            n_jumps += 1
        
        return n_jumps
