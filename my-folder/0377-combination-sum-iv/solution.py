class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        

        def dfs(currsum, memo):
            
            if currsum > target:
                return 0

            if currsum == target:
                return 1
            
            if currsum in memo:
                return memo[currsum]

            count = 0
            for i in range(len(nums)):
                count += dfs(currsum + nums[i], memo)
            memo[currsum] = count
            return count

            
        memo = {}
        return dfs(0, memo)
