class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        """
        dp
        """

        total_sum = sum(nums)

        if total_sum & 1 : return False
        
        subsetsum = total_sum // 2
        
        curr = [False] * (subsetsum+1)
        curr[0] = True

        """
        dp[i][s] -> can num[i..n-1] form s
        if i do:
            curr[j-nums[i]] i.e, can num[i..n-1] form j-nums[i]
            if j < nums[i], we can't take j
            so inner loop is from subsetsum to nums[i]-1
                because inner loop is only when we have 2 choices

            our choices are take or not take
            take is curr[j-nums[i]]
            not take is curr[j]
        """

        for i in range(len(nums)-1,-1,-1):
            for j in range(subsetsum, nums[i]-1,-1):
                curr[j] = curr[j - nums[i]] | curr[j]
        return curr[-1]
            





