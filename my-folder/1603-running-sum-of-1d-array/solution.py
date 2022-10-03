class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = []
        for i,num in enumerate(nums):
            if not ans:
                ans.append(nums[i])
            else:
                ans.append(nums[i] + ans[-1])
        
        return ans
            
