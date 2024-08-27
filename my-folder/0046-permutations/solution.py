class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def dfs(res, ans, nums):
            if len(res) == len(nums):
                ans.append(res.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in res:
                    res.append(nums[i])
                    dfs(res, ans, nums)
                    res.pop()

        dfs([], ans, nums)

        return ans
