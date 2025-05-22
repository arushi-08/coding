class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        
        # given nums
        # call a pair of non-neg arrays (arr1, arr2) monotonic if:
        # length of both arrs are n
        # arr1 is non dec

        # [2,3,2]
        # 0,1,1
        # 2,2,1

        # 0,1,2
        # 2,2,0

        # 

        # monotonic pairs = dp[i][s]
        # last num is s
        # pairs of length i



        # what are the 2 options:
        # nums[i] can be - range(nums[i-1], upto  nums[i+1]+1)
        # nums[i] can be range(nums[i+1], nums[i-1]-1, -1)
        mod = 10**9 + 7
        memo = {}
        def helper(prev, i):
            nonlocal mod

            if i == len(nums):
                return 1
            
            if prev > nums[i]:
                return 0

            if (prev, i) in memo:
                return memo[(prev, i)]

            if i == 0:
                st = 0
            else:
                st = min(prev, nums[i])

            ans = 0
            for j in range(st, nums[i]+1):
                if (
                    (i > 0 and nums[i-1] - prev >= nums[i]-j <= nums[i]) or 
                    (i == 0 and nums[i]-j <= nums[i])
                ):
                    ans += helper(j, i+1)
            memo[(prev, i)] = ans % mod
            return ans
                
        return helper(-1, 0) % mod


