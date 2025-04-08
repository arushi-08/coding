class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l = 0
        r = 0
        n = len(nums)
        n_jumps = 0

        while r < n - 1:

            farthest = 0
            n_jumps += 1
            for ind in range(l, r+1):
                farthest = max(farthest, nums[ind] + ind)
            
            l = r + 1
            r = farthest
        
        return n_jumps
