class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        pprod_left = [1]
        currprod = 1
        for i in range(1, len(nums)):
            currprod *= nums[i-1]
            pprod_left.append(currprod)
        
        pprod_right = [1] * (len(nums))
        currprod = 1
        pprod_right[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            currprod *= nums[i+1]
            pprod_right[i] = currprod
        
        ans = []
        for i in range(len(nums)):
            ans.append(pprod_left[i] * pprod_right[i])
        
        return ans
        

