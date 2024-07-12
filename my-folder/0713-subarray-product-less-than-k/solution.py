class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # 10,5,2,6
        # 1 | 1+1 | 1+1 | 0 | 1

        if not k: return 0

        st = 0
        ans = 0
        currproduct = 1

        for ed in range(len(nums)):
            currproduct *= nums[ed]
            while st <= ed and currproduct >= k:
                currproduct /= nums[st]
                st += 1
            ans += ed - st + 1

        return int(ans)

# 2 3 = 2*1 + 1
# 3 6 = 3*2
# 4 10 = 4*2 + 2
# 5 15 = 5*3
# 6 21 = 6*3 + 3

# 1 2 3 4 5 6
