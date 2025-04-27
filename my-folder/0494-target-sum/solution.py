class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # given int array and int target
        # build expression out of nums by adding 1 of the symbols + and -
        # num of diff exps that evaluate to target

        # passing + or -
        
        """
        + or -
        recursive

        """
        # memo = {}
        # def dfs(i, target):
        #     if i == len(nums):
        #         if target == 0:
        #             return 1
        #         return 0
            
        #     if (i, target) in memo:
        #         return memo[(i, target)]
        #     memo[(i, target)] = dfs(i+1, target + nums[i]) + dfs(i+1, target - nums[i])
        #     return memo[(i, target)]
        # return dfs(0,target)

        # dp[i][target] - num of exps that lead to target in num[i..end]
        """
        n * 2*target array
            -target ... -1 0 1 ... target
        0                  1
        1                1   1
        2              1   2.   1
        3
        we are storing the count of expressinos that sum to target in num[i..end]
            use hashmap as we can get to negative sum (-nums[i])
        curr hashmap stores {currsum : count of expr}
        next hashmap[currsum + nums[i]] += count
        next hashmap[currsum - nums[i]] += count

        return curr[target]
        """
        curr = defaultdict(int)
        curr[0] = 1

        for i in range(len(nums)-1,-1,-1):
            after = defaultdict(int)

            for currtarget, count in curr.items():
                    after[currtarget+nums[i]] += count
                    after[currtarget-nums[i]] += count
            curr = after
        
        return curr[target]
