class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        # maintain range
        # left and right
        # update right to max jump possible from the range
        # update left to right + 1
        # [1,5,1,1,1,5,1,1,1,]
        # O(n)?- yes

        l = 0
        r = 0
        n_jumps = 0
        # [2,3,1,1,4]
        while r < len(nums)-1:
            
            old_r = r
            maxjump = 0
            for i in range(l, r+1):
                maxjump = max(maxjump, i + nums[i])
            r = maxjump
            l = old_r + 1
            n_jumps += 1
        # print('l', 'r', l, r)
        return n_jumps


