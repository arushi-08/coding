class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        # ans[i] such that ans[i] PR ans[i] + 1 == nums[i]

        ans = []
        for i in range(len(nums)):
            j = 0
            while (j | (j+1)) != nums[i] and j < nums[i]:
                j += 1
            
            if j | (j+1) == nums[i]:
                ans.append(j)
            else:
                ans.append(-1)
        
        return ans

