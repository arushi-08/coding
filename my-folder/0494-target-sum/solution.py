class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(currsum, idx, memo):

            if currsum == target and idx == len(nums):
                return 1

            if idx == len(nums):
                return 0
            
            # if idx == 4:
            #     print('4',currsum)

            if (currsum, idx) in memo:
                return memo[(currsum, idx)]

            memo[(currsum, idx)] = (
                dfs(currsum + nums[idx], idx+1, memo) + 
                dfs(currsum - nums[idx], idx+1, memo)
            )
            
            return memo[(currsum, idx)]

        memo = {}
        ans = dfs(0, 0, memo)
        # print(memo)
        return ans
