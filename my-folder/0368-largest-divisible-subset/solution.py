class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        print(nums)
        # 1,2,3,4,5,6
        # 1,2,2,3,2,3
        maxval = 0
        idx = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j]+1
                        parent[i] = j
                        if maxval < dp[i]:
                            idx = i
                            maxval = dp[i]
        
        ans = []
        
        while idx != -1:
            ans.append(nums[idx])
            idx = parent[idx]

        return ans      


